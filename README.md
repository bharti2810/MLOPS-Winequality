Create ev

```bash
conda create -m MLOPS_env
```

created a req file

install the req

```bash
pip install -r requirements.txt
```
Download dataset from:
https://www.youtube.com/redirect?event=live_chat&redir_token=QUFFLUhqbl8wcFlCZ1N4dXRsSUM1QVlBVFdObmQxdC1sUXxBQ3Jtc0ttYXc4RlltN2ZTUVlMaElvMDhsaG9hLWpiTkEtaF9uc1hmVzROVy01SENBN3BoWHl0SlpsdVVSN09vMEVpb3dtS2RnY0xXcUZhdUJ3aXZkNW1iYmV0ZjJzcUFfNEZUT1kwN0x0cWpEc19MN1c0ck1Jdw&q=https%3A%2F%2Fdrive.google.com%2Fdrive%2Ffolders%2F18zqQiCJVgF7uzXgfbIJ-04zgz1ItNfF5%3Fusp%3Dsharing


```
git init
```

```
dvc init
```
```
dvc add data_given/winequality.csv
```

```
git add .
```

```
git commit -m "first commit"
```

```
git remote add origin https://github.com/bharti2810/MLOPS-Winequality.git
git branch -M main
git push -u origin main
```