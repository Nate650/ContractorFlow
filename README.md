# How to execute the tests

1. Clone this repository

```
git clone https://github.com/Nate650/ContractorFlow.git
```

2. Navigate to top-level `ContractorFlow` directory

```
cd ContractorFlow
```

3. Install dependencies using pip

```
pip install -r requirements.txt
```
> If you are on a different Python version (e.g., Python 3.x), you may have to replace `pip` with `pip3`

4. Run the tests

```
pytest -v -s .\tests\test_opportunity.py --html=reports/report.html
```
> After the tests are finished, the results will be viewable in `reports/report.html`
