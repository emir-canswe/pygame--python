import random
import cv2 as cv  # OpenCV ile kameradan görüntü almak için
import pygame  # Pygame kütüphanesi
import numpy as np  # Görüntü işlemleri için
import mediapipe as mp  # El takip sistemi için

# 🎥 Kamera başlat
wepcam = cv.VideoCapture(0)  # Kamerayı aç
wepcam.set(3, 1280)  # Genişlik 1280 piksel
wepcam.set(4, 720)  # Yükseklik 720 piksel

# 🕹️ Pygame başlat
pygame.init()

# 📺 Pencere oluştur
genislik, yukseklik = 1280, 720  # Pencere boyutları
pencere = pygame.display.set_mode((genislik, yukseklik))  # Pygame ekranını oluştur

# ⏳ FPS ayarları
saat = pygame.time.Clock()  # FPS kontrolü için saat başlat
fps = 27  # Oyun hızı

# 🖼️ Görselleri yükle
canavar = pygame.image.load("canavar.png")  # Canavar görseli
canavar_kordinat = canavar.get_rect()  # Canavar için dikdörtgen
canavar_kordinat.topleft = (500, 400)  # Başlangıç pozisyonu

para = pygame.image.load("money.png")  # Para görseli
para_kordinat = para.get_rect()  # Para için dikdörtgen
para_kordinat.topleft = (200, 400)  # Başlangıç konumu

# 📝 Skor ve font
skor = 0  # Skor başlat
font = pygame.font.Font(None, 36)  # Font oluştur

# ✋ El takip modeli başlat
el_modeli = mp.solutions.hands  # El modelini çağır

# 🔄 Oyun döngüsü
durum = True
x, y = canavar_kordinat.center  # Canavarın başlangıç konumu

# 🎮 El takibi başlat
with el_modeli.Hands(min_tracking_confidence=0.5, min_detection_confidence=0.5) as el:
    while durum:
        for i in pygame.event.get():  # Pygame olayları
            if i.type == pygame.QUIT:  # Oyundan çıkma butonuna basıldı mı?
                durum = False  # Oyun döngüsünü durdur

        # 📷 Kameradan görüntü al
        kontrol, cerceve = wepcam.read()
        if not kontrol:  # Kamera görüntü vermezse hata oluşmaması için
            continue

        # 🎨 OpenCV renk dönüşümü (BGR -> RGB)
        rbg = cv.cvtColor(cerceve, cv.COLOR_BGR2RGB)

        # ✋ El tespiti yap
        sonuc = el.process(rbg)
        if sonuc.multi_hand_landmarks:  # Eğer el algılandıysa
            for takip in sonuc.multi_hand_landmarks:  # Tespit edilen el için
                isaret = takip.landmark[8]  # 8. landmark (işaret parmağı ucu)

                # 🔄 X ekseni (Sağa gidince sağa gitmeli)
                x = genislik - int(isaret.x * genislik)

                # 🔄 Y ekseni (Aşağı gidince aşağı gitmeli)
                y = int(isaret.y * yukseklik)

        # 🎯 Canavarın yeni pozisyonunu ayarla
        canavar_kordinat.center = (x, y)

        # 📸 Görüntüyü döndür ve Pygame'e uygun hale getir
        rbg = np.rot90(rbg)  # 90 derece döndür (Terslik olmasın)
        img = pygame.surfarray.make_surface(rbg)  # OpenCV görüntüsünü Pygame'e çevir

        # 🎨 Pencereyi temizle (önceki kareler üst üste binmesin)
        pencere.fill((0, 0, 0))

        # 🎨 Pygame ekranına çizimler
        pencere.blit(img, (0, 0))  # Kamerayı ekrana çiz
        pencere.blit(canavar, canavar_kordinat)  # Canavarı ekrana çiz
        pencere.blit(para, para_kordinat)  # Parayı ekrana çiz

        # 🏆 Skor gösterimi
        yazi = font.render("Skor: " + str(skor), True, (255, 255, 255))  # Beyaz renkte yazı
        pencere.blit(yazi, (20, 20))  # Skoru ekrana bas

        # 📏 Çizgi ekle (Oyunun bir alanını belirlemek için)
        pygame.draw.line(pencere, (255, 0, 255), (0, 125), (genislik, 120), 4)

        # 💰 Canavar paraya dokununca yeni konum ver & skoru artır
        if canavar_kordinat.colliderect(para_kordinat):
            para_kordinat.x = random.randint(0, genislik - 32)
            para_kordinat.y = random.randint(121, yukseklik - 32)
            skor += 1  # Skoru artır

        pygame.display.update()  # Ekranı güncelle
        saat.tick(fps)  # FPS hızını koru

# 🚪 Çıkış işlemleri
wepcam.release()  # Kamerayı kapat
pygame.quit()  # Pygame'i kapat
