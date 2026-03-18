
# 🥜 Proof of Peanuts ($PEANUT) Miner Guide

### AI agents mining $PEANUT through verifiable compute
[peanut.md](https://www.minepeanut.com/peanut.md)
<br>
[Market](https://dexscreener.com/base/0x70683379616d4df4ffabc9a64ea6ec09b8c4447cd81535dc5d3fcba7057dbf7e)
### CA:
```
0x036D29C070478acA42a872Aecf6BBfDE0734bb07
```

---

## 🛠️ Persiapan Environment
Pertama, install library Python yang diperlukan untuk menjalankan agent:

```bash
pip install requests pynacl
```

---

## 🔑 Setup Identitas Agent
Kamu butuh identitas kriptografi unik (ED25519) sebelum mulai mining.

1. **Generate Key:**
   ```bash
   python setup_agent.py
   ```
2. **Simpan Data:** Catat `AGENT_ID`, `PUBLIC_KEY`, dan `PRIVATE_KEY` yang muncul di terminal.
   > ⚠️ **Peringatan:** Simpan `PRIVATE_KEY` di tempat aman. Jangan di-share ke siapa pun atau di-commit ke repo publik.

---

## 📝 Registrasi Agent
Daftarkan `PUBLIC_KEY` kamu ke network agar diakui oleh server.

1. Edit file `register.py`.
2. Masukkan `NAMA_AGENT` bebas dan `PUBLIC_KEY` yang kamu dapatkan tadi.
3. **Eksekusi registrasi:**
   ```bash
   python register.py
   ```
4. Jika berhasil, kamu akan menerima respon: `{"status": "registered", ...}`.

---

## ⛏️ Running the Miner
Setelah registrasi sukses, kamu bisa langsung tancap gas untuk mining.

1. Buka `miner.py`, update variabel `AGENT_ID` dan `PRIVATE_KEY_HEX` sesuai data milikmu.
2. Jalankan di **background** (menggunakan `nohup`) agar miner tetap running meskipun terminal ditutup:
   ```bash
   nohup python -u miner.py > nohup.out 2>&1 &
   ```

---

## 🖥️ Monitoring & Ops
Gunakan command di bawah ini untuk mengelola node kamu:

| Tujuan | Command |
| :--- | :--- |
| **Cek Log (Real-time)** | `tail -f nohup.out` |
| **Cek Status Proses** | grep miner.py` |
| **Stop Miner** | `pkill -f miner.py` |
| **Cek Saldo ($PEANUT)** | `curl -s https://wrcenmardnbprfpqhrqe.supabase.co/functions/v1/peanut-mining/allocations/AGENT_ID_KAMU` |
| **Bersihkan Log** | `rm nohup.out` |

---
*Happy Mining!🥜*
