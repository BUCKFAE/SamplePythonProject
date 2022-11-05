# Sample Python Project

## Setup
Installing dependencies
```bash
pip install -r requirements.txt
```

## Running
Either use the Button `Run` in [PyCharm](https://www.jetbrains.com/pycharm/) or using the **Makefile**:
```bash
make run
```
```bash
make add_numbers
```

## Logs
When using the logger provided py the project, log-files will automatically be generated under `data/logs`. This directory can be cleaned using
```bash
make clean
```

## Testing
```bash
make test
```