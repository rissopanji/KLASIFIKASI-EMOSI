import papermill as pm

notebooks = [
    "07. Pemodelan Data (Data Mining)/01.LSTM.ipynb",
    "07. Pemodelan Data (Data Mining)/02.CNN.ipynb",
    "07. Pemodelan Data (Data Mining)/03.BILSTM.ipynb",
    "07. Pemodelan Data (Data Mining)/04.CNN-LSTM.ipynb",
    "07. Pemodelan Data (Data Mining)/05.CNN-BILSTM.ipynb",
    "07. Pemodelan Data (Data Mining)/06.LSTM-CNN.ipynb",
    "07. Pemodelan Data (Data Mining)/07.BILSTM-CNN.ipynb"
]

for notebook in notebooks:
    pm.execute_notebook(
        notebook,
        notebook
    )
