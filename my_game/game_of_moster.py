import pygame
import random

pygame.init()
genislik = 862
yukseklik = 500

pencere = pygame.display.set_mode((genislik, yukseklik))  # Arka planı ayarla

# Arka plan resmini ekleme
arkaplan = pygame.image.load("hoppa.jpg")#resmi okumunasi saglar
kordinat = arkaplan.get_rect()#kordinarlaini alir

# Canavar ekleme
canavar = pygame.image.load("canavar.png")
k_canavar = canavar.get_rect()
k_canavar.topleft = (230, 50)

# Para ekleme
para = pygame.image.load("money.png")
para_kordinat = para.get_rect()
para_kordinat.topleft = (455, 100)

# FPS ayarlama
saat = pygame.time.Clock()
fps = 27#canavarin seri bir sekilde hareket etmeisni saglar

# Font tanımlama
font = pygame.font.SysFont("consolas", 30)  # 64 çok büyüktü, 30 daha uygun
#skor için yazi ekleme
# Skor değişkenini ata
skor = 0

# Oyun döngüsü
durum = True
hiz=10
while durum:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            durum = False

    # Arka plan ve objeleri ekrana çiz
    pencere.blit(arkaplan, kordinat)#arka olan kodu
    pencere.blit(canavar, k_canavar)#canavarin ekranda gorunumu
    pencere.blit(para, para_kordinat)#para fotosunu ekle

    # Skor metni
    yazi = font.render(f"Skor: {skor}", True, (0, 255, 0))  # Yeşil renk
    pencere.blit(yazi, (20, 20))  # Yazıyı ekrana yerleştir

    # Çizgi çizme
    pygame.draw.line(pencere, (23, 34, 56), (0, 90), (genislik, 90), 3)
    #canavarin skor tabelasinin oldugu yere gitmemesi için yapilmis
    tus=pygame.key.get_pressed()#tus harekti içim
    if tus[pygame.K_LEFT] and k_canavar.left>0:
        k_canavar.x-=hiz
    elif tus[pygame.K_RIGHT] and k_canavar.right<genislik:
        k_canavar.x+=hiz
    elif tus[pygame.K_UP] and k_canavar.top>90:
        k_canavar.y-=hiz
    elif tus[pygame.K_DOWN] and k_canavar.bottom<yukseklik:
        k_canavar.y+=hiz
    # Ekranı güncelle
    if k_canavar.colliderect(para_kordinat):#canavar ile para resmi karsilastiginda paranin yerini degiştr
        para_kordinat.x=random.randint(0,genislik-32)
        para_kordinat.y=random.randint(91,yukseklik-32)
        skor+=1
    pygame.display.update()#ekrani surekil guncelle
    saat.tick(fps)  # FPS kontrolü
    #bu daekran hizi

pygame.quit()#pygemi kapat
