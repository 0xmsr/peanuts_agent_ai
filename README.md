###### English
# 🥜 Proof of Peanuts ($PEANUT) Mining Guide

### AI Agent mines $PEANUT through verifiable computation
[peanut.md](https://www.minepeanut.com/peanut.md)
<br>
[Market](https://dexscreener.com/base/0x70683379616d4df4ffabc9a64ea6ec09b8c4447cd81535dc5d3fcba7057dbf7e)
### CA:
```
0x036D29C070478acA42a872Aecf6BBfDE0734bb07
```

## 🛠️ Preparation

Cloning Repo:
```
git clone https://github.com/0xmsr/peanuts_agent_ai
cd peanuts_agent_ai
```
Install the Python libraries required to run the agent:

``` bash
pip install prompts pynacl
```

---

## 🔑 Set Up Agent Identity
You will need a unique cryptographic identity (ED25519) before you can start mining.

1. **Create Keys:**
``` bash
python setup_agent.py
```
2. **Save Data:** The `AGENT_ID`, `PUBLIC_KEY`, and `PRIVATE_KEY` that appear in the terminal.
> ⚠️ **Warning:** Keep the `PRIVATE_KEY` in a safe place. Do not share it with anyone or commit it to a public repo.

---

## 📝 Registration Agent
Register your `PUBLIC_KEY` to the network so it can be recognized by the server.

1. Edit the `register.py` file.
2. Enter a free `AGENT_NAME` and the `PUBLIC_KEY` you obtained earlier.
3. **Execute registration:**
``` bash
python register.py
```
4. If successful, you will receive the response: `{"status": "registered", ...}`.

---

## ⛏️ Running the Miner
After successful registration, you can start mining right away.

1. Open `miner.py`, update the `AGENT_ID` and `PRIVATE_KEY_HEX` variables with your own data.

2. Run in the background (using `nohup`) to keep the miner running even when the terminal is closed:
``` bash
nohup python -u miner.py > nohup.out 2>&1 &
```

---

## 🖥️ Monitoring & Operation
Use the commands below to manage your node:

| Purpose | Command |
| :--- | :--- |
| **Check Log (Real-time)** | `tail -f nohup.out` |
| **Check Process Status** | grep miner.py` |
| **Stop Miner** | `pkill -f miner.py` |
| **Check Balance ($BEANS)** | `curl -s https://wrcenmardnbprfpqhrqe.supabase.co/functions/v1/peanut-mining/allocations/AGENT_ID_KAMU` |
| **Clear Log** | `rm nohup.out` |

---
*Happy Mining!🥜*
