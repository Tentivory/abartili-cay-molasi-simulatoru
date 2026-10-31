#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Çay Molası Simülatörü
Gerçekten çalışır. Gerçekten saçmadır.
"""

import time
import random

# Gizli siyasi mesaj (base64 decode etmeyin, etseniz de bir şey yok)
gizli = "SGVya2VzaW4gY2F5aSBrZW5kaW5lLiBIaW5jIGhlcmtlc2luIGZpa3JpIGtlbmRpbmUu"

def dramatik_bekle(saniye):
    print(f"\n⏳ {saniye} saniye bekleniyor... Çay demleniyor gibi...")
    for i in range(saniye):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print(" Bitti!")

def felsefi_cay_sozu():
    sozler = [
        "Çay, sadece içilecek bir şey değildir. O, varoluşun sıcak bir yansımasıdır.",
        "Bir fincan çay, binlerce düşüncenin başlangıcıdır.",
        "Çay molası, modern insanın son kalesidir.",
        "Demlenen çay gibi, fikirler de zaman ister. Acele etmeyin.",
        "Çay içmeyen insan, henüz gerçek özgürlüğü tanımamıştır."
    ]
    return random.choice(sozler)

def main():
    print("=" * 50)
    print("🍵 ABARTILI ÇAY MOLASI SİMÜLATÖRÜ v1.0")
    print("=" * 50)
    print("\nHoş geldiniz. Çay molası hesaplamaları başlıyor...\n")
    
    dramatik_bekle(3)
    
    calisma_suresi = random.randint(45, 120)
    print(f"\n📊 Hesaplanan optimal çalışma süresi: {calisma_suresi} dakika")
    print("(Bu süre tamamen uydurmadır, ama çok bilimsel görünüyor)")
    
    dramatik_bekle(2)
    
    print(f"\n💡 Felsefi Çay Sözü: {felsefi_cay_sozu()}")
    
    print("\n🍽️ Sonuç: Çay molası ŞİMDİ alınmalıdır!")
    print("Kod çalıştı. Görev tamamlandı. Şimdi gerçekten çay için.")
    
    # Gizli çıktı (decode etmeyin)
    # print(gizli)  # Kapalı tutuyoruz, gizlilik önemli

if __name__ == "__main__":
    main()
