import pygame  # Pygame modülünü içeri aktarıyoruz (oyunun grafik, ses, kontrol işlemleri için).
import random  # Rastgele sayılar üretmek için 'random' modülünü ekliyoruz.

pygame.init()  # Pygame kütüphanesini başlatıyoruz. Bu olmadan Pygame fonksiyonları çalışmaz.

# --- Oyun penceresi boyutları:
genislik = 862  # Pencere genişliği
yukseklik = 572  # Pencere yüksekliği
pencere = pygame.display.set_mode((genislik, yukseklik))  # Oyunun oynanacağı pencereyi ayarlıyoruz.

# --- Arka plan resmi yükleme:
arka_plan = pygame.image.load(r"C:\Users\MSİ\Desktop\python_code\oyunlar\final_game.jpg")  # Arka plan resmini yüklüyoruz.
arka_kordinat = arka_plan.get_rect()  # Arka planın kordinatlarını alıyoruz.

# --- Ana karakter (canavar):
canavar = pygame.image.load(r"C:\Users\MSİ\Desktop\python_code\oyunlar\ayi.png")  # Ana karakterimizin (ayı resmi) yüklenmesi.
canavar_kordinat = canavar.get_rect()  # Ana karakterin dikdörtgen şeklindeki kordinatlarını alıyoruz.
canavar_kordinat.topleft = (200, 200)  # Ana karakterin başlangıçtaki konumunu belirtiyoruz.

# --- Minik canavar (skor artırıyor):
minik = pygame.image.load(r"C:\Users\MSİ\Desktop\python_code\oyunlar\money.png")  # Minik canavar resmini yüklüyoruz.
minik_kordinat = minik.get_rect()  # Minik canavarın kordinatlarını alıyoruz.
minik_kordinat.topleft = (300, 300)  # Minik canavarın başlangıç konumunu belirtiyoruz.

# --- Kötü canavarlar (skor azaltıyor):
kotu_canavar1 = pygame.image.load(r"C:\Users\MSİ\Desktop\python_code\oyunlar\canavar.jpg")  # Birinci kötü canavarı yükleme.
kotu_canavar1_kordinat = kotu_canavar1.get_rect()  # Birinci kötü canavarın kordinatlarını alıyoruz.
kotu_canavar1_kordinat.topleft = (random.randint(0, genislik-32), random.randint(60, yukseklik-32))  # Başlangıç konumu rastgele.

kotu_canavar2 = pygame.image.load(r"C:\Users\MSİ\Desktop\python_code\oyunlar\canavar.jpg")  # İkinci kötü canavarı yükleme.
kotu_canavar2_kordinat = kotu_canavar2.get_rect()  # İkinci kötü canavarın kordinatlarını alıyoruz.
kotu_canavar2_kordinat.topleft = (random.randint(0, genislik-32), random.randint(60, yukseklik-32))  # Rastgele konum.


kotu_canavar3 = pygame.image.load(r"C:\Users\MSİ\Desktop\python_code\oyunlar\canavar.jpg")  # İkinci kötü canavarı yükleme.
kotu_canavar3_kordinat = kotu_canavar2.get_rect()  # İkinci kötü canavarın kordinatlarını alıyoruz.
kotu_canavar3_kordinat.topleft = (random.randint(0, genislik-32), random.randint(60, yukseklik-32)) 


kotu_canavar4 = pygame.image.load(r"C:\Users\MSİ\Desktop\python_code\oyunlar\canavar.jpg")  # İkinci kötü canavarı yükleme.
kotu_canavar4_kordinat = kotu_canavar2.get_rect()  # İkinci kötü canavarın kordinatlarını alıyoruz.
kotu_canavar4_kordinat.topleft = (random.randint(0, genislik-32), random.randint(60, yukseklik-32)) 



# --- FPS ayarlama:
saat = pygame.time.Clock()  # Oyunun hızını kontrol etmek için 'Clock' nesnesi oluşturuyoruz.
fps = 60  # Oyun 60 FPS hızında çalışacak.

# --- Skor göstergesi ve yazı tipi ayarlama:
font = pygame.font.SysFont("consolas", 30)  # Skoru göstermek için yazı tipi ayarlıyoruz.
skor = 3  # Oyuncunun başlangıç skoru.

# --- Oyun durumu ve hareket hızları:
durum = True  # Oyun devam ettiği sürece bu değişken 'True' kalacak.
hiz = 10  # Ana karakterin hareket hızı.
hiz_kotu_canavar = 5  # Kötü canavarların hareket hızı.

# --- Kötü canavarların başlangıç yönleri (x ve y ekseninde sağ/sol yukarı/aşağı hareket):
kotu_canavar1_hiz_x = random.choice([-hiz_kotu_canavar, hiz_kotu_canavar])  # Birinci kötü canavarın x ekseninde hareket yönü.
kotu_canavar1_hiz_y = random.choice([-hiz_kotu_canavar, hiz_kotu_canavar])  # Birinci kötü canavarın y ekseninde hareket yönü.

kotu_canavar2_hiz_x = random.choice([-hiz_kotu_canavar, hiz_kotu_canavar])  # İkinci kötü canavarın x ekseninde hareket yönü.
kotu_canavar2_hiz_y = random.choice([-hiz_kotu_canavar, hiz_kotu_canavar])  # İkinci kötü canavarın y ekseninde hareket yönü.


kotu_canavar3_hiz_x = random.choice([-hiz_kotu_canavar, hiz_kotu_canavar])  # İkinci kötü canavarın x ekseninde hareket yönü.
kotu_canavar3_hiz_y = random.choice([-hiz_kotu_canavar, hiz_kotu_canavar])  # İkinci kötü canavarın y ekseninde hareket yönü.

kotu_canavar4_hiz_x = random.choice([-hiz_kotu_canavar, hiz_kotu_canavar])  # İkinci kötü canavarın x ekseninde hareket yönü.
kotu_canavar4_hiz_y = random.choice([-hiz_kotu_canavar, hiz_kotu_canavar])  # İkinci kötü canavarın y ekseninde hareket yönü.


# --- Oyun Döngüsü:
while durum:  # Oyun devam ettiği sürece bu döngü çalışacak.
    for i in pygame.event.get():  # Oyun içindeki olayları kontrol ediyoruz (örn. pencereyi kapatma).
        if i.type == pygame.QUIT:  # Kullanıcı pencereyi kapatmak isterse:
            durum = False  # Oyun döngüsünden çıkış yapılır.

    # --- Ekrana resimleri çiziyoruz:
    pencere.blit(arka_plan, arka_kordinat)  # Arka planı pencereye çiziyoruz.
    pencere.blit(canavar, canavar_kordinat)  # Ana karakteri pencereye çiziyoruz.
    pencere.blit(minik, minik_kordinat)  # Minik canavarı pencereye çiziyoruz.
    pencere.blit(kotu_canavar1, kotu_canavar1_kordinat)  # Birinci kötü canavarı pencereye çiziyoruz.
    pencere.blit(kotu_canavar2, kotu_canavar2_kordinat)  # İkinci kötü canavarı pencereye çiziyoruz.
    pencere.blit(kotu_canavar3, kotu_canavar3_kordinat)  # İkinci kötü canavarı pencereye çiziyoruz.
    pencere.blit(kotu_canavar4, kotu_canavar4_kordinat)  # İkinci kötü canavarı pencereye çiziyoruz.
    # --- Skoru yazdırıyoruz:
    yazi = font.render(f"Skor: {skor}", True, (100, 100, 100))  # Skor yazısını ayarlıyoruz.
    pencere.blit(yazi, (20, 20))  # Skor yazısını ekranın sol üst köşesine ekliyoruz.

    # --- Üst kısma bir çizgi çiziyoruz (oyun alanını ayırmak için):
    pygame.draw.line(pencere, (10, 200, 0), (0, 60), (genislik, 60), 3)

    # --- Ana karakterin klavye tuşları ile hareket etmesi:
    tus = pygame.key.get_pressed()  # Kullanıcının hangi tuşa bastığını kontrol ediyoruz.
    if tus[pygame.K_LEFT] and canavar_kordinat.x > 10:  # Sol ok tuşu: Sola hareket.
        canavar_kordinat.x -= hiz
    elif tus[pygame.K_RIGHT] and canavar_kordinat.x < genislik-70:  # Sağ ok tuşu: Sağa hareket.
        canavar_kordinat.x += hiz
    elif tus[pygame.K_UP] and canavar_kordinat.y > 60:  # Yukarı ok tuşu: Yukarı hareket.
        canavar_kordinat.y -= hiz
    elif tus[pygame.K_DOWN] and canavar_kordinat.y < yukseklik-70:  # Aşağı ok tuşu: Aşağı hareket.
        canavar_kordinat.y += hiz

    # --- Kötü canavarların hareketleri:
    kotu_canavar1_kordinat.x += kotu_canavar1_hiz_x  # Birinci kötü canavarın x ekseninde hareketi.
    kotu_canavar1_kordinat.y += kotu_canavar1_hiz_y  # Birinci kötü canavarın y ekseninde hareketi.

    kotu_canavar2_kordinat.x += kotu_canavar2_hiz_x  # İkinci kötü canavarın x ekseninde hareketi.
    kotu_canavar2_kordinat.y += kotu_canavar2_hiz_y  # İkinci kötü canavarın y ekseninde hareketi.

    kotu_canavar3_kordinat.x += kotu_canavar3_hiz_x  # İkinci kötü canavarın x ekseninde hareketi.
    kotu_canavar3_kordinat.y += kotu_canavar3_hiz_y  # İkinci kötü canavarın y ekseninde hareketi.

    kotu_canavar4_kordinat.x += kotu_canavar4_hiz_x  # İkinci kötü canavarın x ekseninde hareketi.
    kotu_canavar4_kordinat.y += kotu_canavar4_hiz_y  # İkinci kötü canavarın y ekseninde hareketi.


    # --- Kötü canavarların ekran sınırlarında yön değiştirmesi:
    if kotu_canavar1_kordinat.x <= 0 or kotu_canavar1_kordinat.x >= genislik - 32:  # X sınırı.
        kotu_canavar1_hiz_x *= -1  # Yön değiştirme (sağ-sol).
    if kotu_canavar1_kordinat.y <= 60 or kotu_canavar1_kordinat.y >= yukseklik - 32:  # Y sınırı.
        kotu_canavar1_hiz_y *= -1

    if kotu_canavar2_kordinat.x <= 0 or kotu_canavar2_kordinat.x >= genislik - 32:
        kotu_canavar2_hiz_x *= -1
    if kotu_canavar2_kordinat.y <= 60 or kotu_canavar2_kordinat.y >= yukseklik - 32:
        kotu_canavar2_hiz_y *= -1
    
    if kotu_canavar3_kordinat.x <= 0 or kotu_canavar3_kordinat.x >= genislik - 32:
        kotu_canavar3_hiz_x *= -1
    if kotu_canavar3_kordinat.y <= 60 or kotu_canavar3_kordinat.y >= yukseklik - 32:
        kotu_canavar3_hiz_y *= -1

    if kotu_canavar4_kordinat.x <= 0 or kotu_canavar4_kordinat.x >= genislik - 32:
        kotu_canavar4_hiz_x *= -1
    if kotu_canavar4_kordinat.y <= 60 or kotu_canavar4_kordinat.y >= yukseklik - 32:
        kotu_canavar4_hiz_y *= -1

    # --- Ana karakterin minik canavar ve kötü canavarlarla temas etmesi:
    if canavar_kordinat.colliderect(minik_kordinat):  # Ana karakter minik canavara dokunursa:
        skor += 1  # Skor artırılır.
        minik_kordinat.topleft = (random.randint(0, genislik-32), random.randint(60, yukseklik-32))  # Minik canavar rastgele yeni konuma gider.
    if canavar_kordinat.colliderect(kotu_canavar1_kordinat):  # Ana karakter birinci kötü canavara dokunursa:
        skor -= 1  # Skor 1 azalır.
        kotu_canavar1_kordinat.topleft = (random.randint(0, genislik-32), random.randint(60, yukseklik-32))  # Birinci kötü canavar yeni bir rastgele konuma gider.

    if canavar_kordinat.colliderect(kotu_canavar2_kordinat):  # Ana karakter ikinci kötü canavara dokunursa:
        skor -= 1  # Skor 1 azalır.
        kotu_canavar2_kordinat.topleft = (random.randint(0, genislik-32), random.randint(60, yukseklik-32))  # İkinci kötü canavar yeni bir rastgele konuma gider.

    if canavar_kordinat.colliderect(kotu_canavar3_kordinat):  # Ana karakter ikinci kötü canavara dokunursa:
        skor -= 1  # Skor 1 azalır.
        kotu_canavar3_kordinat.topleft = (random.randint(0, genislik-32), random.randint(60, yukseklik-32))  # İkinci kötü canavar yeni bir rastgele konuma gider.
    


    if canavar_kordinat.colliderect(kotu_canavar4_kordinat):  # Ana karakter ikinci kötü canavara dokunursa:
        skor -= 1  # Skor 1 azalır.
        kotu_canavar4_kordinat.topleft = (random.randint(0, genislik-32), random.randint(60, yukseklik-32))  # İkinci kötü canavar yeni bir rastgele konuma gider.


    # --- Oyuncunun kaybetme durumu:
    if skor <= 0:  # Skor sıfır veya daha aşağı düştüğünde:
        font_lose = pygame.font.SysFont("consolas", 60)  # Kaybetme ekranı için büyük bir yazı fontu belirleniyor.
        lose_text = font_lose.render("GAME OVER", True, (255, 0, 0))  # "GAME OVER" metni kırmızı renk ile hazırlanıyor.
        pencere.blit(lose_text, (genislik // 3, yukseklik // 2))  # "GAME OVER" yazısı ekranın ortasına konumlanıyor.
        pygame.display.flip()  # Ekran güncelleniyor.
        pygame.time.delay(3000)  # 3 saniye bekliyoruz.
        durum = False  # Oyun sona erdiriliyor.

    pygame.display.update()  # Oyunun ekranı her karede (frame) güncelleniyor.
    saat.tick(fps)  # Oyun hızını belirleyen FPS ayarına uygun olarak bekletme yapıyoruz.

pygame.quit()  # Oyun kapanınca Pygame modülünü kapatıyoruz.
