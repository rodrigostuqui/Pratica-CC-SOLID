from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_criar_conta():
    response = client.post(
        "/contas",
        json={"banco": "01", "agencia": "01", "conta": "01"},
    )
    assert response.status_code == 201
    assert response.json() == {"id": 1}


def test_creditar_conta_erro():
    client.post(
        "/contas",
        json={"banco": "01", "agencia": "01", "conta": "01"},
    )
    response = client.put("contas/1/credito?valor=10")
    assert response.status_code == 400
    assert response.json() == {"detail": "O valor especificado é maior que o saldo"}


def test_consulta_saldo():
    client.post(
        "/contas",
        json={"banco": "01", "agencia": "01", "conta": "01"},
    )
    response = client.get("contas/1/saldo")
    assert response.status_code == 200
    assert response.json() == {"valor": 0}


def test_consulta_saldo_erro():
    client.post(
        "/contas",
        json={"banco": "01", "agencia": "01", "conta": "01"},
    )
    response = client.get("contas/20/saldo")
    assert response.status_code == 400
    assert response.json() == {"detail": "Conta Não existe no banco"}


def test_creditar_conta():
    client.post(
        "/contas",
        json={"banco": "01", "agencia": "01", "conta": "01"},
    )
    response = client.put("contas/1/credito?valor=0")
    assert response.status_code == 200


def test_debitar_conta():
    client.post(
        "/contas",
        json={"banco": "01", "agencia": "01", "conta": "01"},
    )
    response = client.put("contas/1/debito?valor=20")
    assert response.status_code == 200
