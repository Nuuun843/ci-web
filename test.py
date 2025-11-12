def test_nim_in_html():
    with open("index.html", "r", encoding="utf-8") as f:
        content = f.read()
    assert "230411100081" in content, "NIM tidak ditemukan di halaman HTML"

def test_nama_in_html():
    with open("index.html", "r", encoding="utf-8") as f:
        content = f.read()
    assert "Nor Ahmad Mahmud" in content, "Nama tidak ditemukan di halaman HTML"
