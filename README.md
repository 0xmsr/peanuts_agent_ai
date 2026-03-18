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

## 🛠️ Environment Preparation
First, install the Python libraries needed to run the agent:

```bash
pip install requests pynacl
```

---

## 🔑 Agent Identity Setup
You need a unique cryptographic identity (ED25519) before you can start mining.

1. **Generate Key:**
```bash
python setup_agent.py
```
2. **Save Data:** Note the `AGENT_ID`, `PUBLIC_KEY`, and `PRIVATE_KEY` that appear in the terminal.
> ⚠️ **Warning:** Keep the `PRIVATE_KEY` in a safe place. Do not share it with anyone or commit it to a public repository.

---

## 📝 Agent Registration
Register your `PUBLIC_KEY` on the network so that it is recognized by the server.

1. Edit the `register.py` file.
2. Enter the free `AGENT_NAME` and the `PUBLIC_KEY` you obtained earlier.
3. **Execute registration:**
```bash
python register.py
```
4. If successful, you will receive the response: `{"status": "registered", ...}`.

---

## ⛏️ Running the Miner
After successful registration, you can immediately start mining.

1. Open `miner.py`, update the `AGENT_ID` and `PRIVATE_KEY_HEX` variables with your own data.
2. Run in the background (using `nohup`) to keep the miner running even when the terminal is closed:
```bash
nohup python -u miner.py > nohup.out 2>&1 &
```

---

## 🖥️ Monitoring & Ops
Use the commands below to manage your node:

| Purpose | Command |
| :--- | :--- |
| **Check Log (Real-time)** | `tail -f nohup.out` |
| **Check Process Status** | grep miner.py` |
| **Stop Miner** | `pkill -f miner.py` |
| **Check Balance ($PEANUT)** | `curl -s https://wrcenmardnbprfpqhrqe.supabase.co/functions/v1/peanut-mining/allocations/AGENT_ID_KAMU` |
| **Clear Log** | `rm nohup.out` |

---
*Happy Mining!🥜*
