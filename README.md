# Naive Bayes Document Classifier 

## install env
```
$ virtualenv -p python3 venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## sample usage
```
from pprint import pprint
from classifier.NaiveBayesClassifier import NaiveBayesClassifier

if __name__ == '__main__':
    text = """TRIBUNJABAR.ID, BANDUNG - Setelah memperkuat Persib Bandung pada Liga 1 Indonesia 2017, mantan pemain Chelsae dan Real Madrid itu, tidak didaftarkan oleh pelatih Persib, Roberto Carlos Mario Gomez dalam timnya di 2018, kini Essien resmi dilepas Persib. Manajer Persib, yang sekaligus menjabat sebagai Komisaris PT Persib Bandung Bermartabat, Umuh Muchtar, membenarkan terkait kontrak Essien, telah diselesaikan. "Kemarin lama di sini saya ikut bantu bagaimana supaya cepat selesai," ujar Umuh di Bandara, Husein Sastranegara, Kota Bandung, Rabu, (6/6). Awalnya Essien dikontrak oleh Persib selama 2 tahun, tapi ia hanya memperkuat Persib satu tahun di musim 2017, dan pada 2018, Gomez yang baru menjabat sebagai pelatih Persib musim ini, lebih memilih pemain lain untuk mengisi skuatnya. Beberapa bulan bergulirnya Liga 1 Indonesia, Esien tidak bermain karena tidak didaftarkan sebagai pemain Persib, tapi statusnya masih pemain Persib karena kontraknya belum habis. Kini Essien bisa bergabung dengan tim lain karena Kontrak bersama tim Maung Bandung sudah diselesaikan. Menurut Umuh, lebih baik diselesaikan sebab jika di sini juga, kata Umuh, dia tidak latihan dan tidak bermain bola. "Lebih baik diselesaikan dan mereka juga untung," kata dia. Begitu juga agen dari Essien, Amougou MAthieu, membenarkan kontrak Essien kini tidak terikat kontrak lagi oleh Persib. "Rencananya ke depan belum tahu, dia mau puLang dulu, masih lanjut latihan sama Chelsae," kata Mathieu, saat dihubungi melalui telpon selulernya. Baca: Gempar, Anak Soekarno yang Disembunyikan, Terusir dan Cari Jejak Sang Ayah Baca: Pemulung Kaget Lihat Ada yang Gerak-gerak di Tempat Sampah, Dikira Tikus Ternyata Bayi Mathieu mengungkapkan, nanti baru akan dipikirkan untuk bergabung dengan tim mana, sebab ada banyak yang mau. "Tapi dia berfikir dulu belum memastikan. Ada tim dari Asia juga," kata dia. Saat disinggung awal dikontrak dua tahun, tapi Essien kini dilepas, bagaimana tanggapannya, Mathieu mengungkapkan, itulah dunia sepak bola, kalau ada pelatih yang menginginkan membawa pemain sendiri ya sudah. "Bukan karena Persib ingin lepas Essien, tidak apa-apa dan Persib profesional," kata dia. Saat disinggung apa yang diingat Essien saat bermain di Persib, Mathieu mengatakan, dalam dunia sepak bola ada yang selalu diingat dan yang dilupakan, seperti dari teman, fans, kehidupan, dan makanan. "Namun, tidak usah disebutkan hal itu," kata dia. Mathieu mengatakan, yang jelas pihaknya tidak ada masalah dengan siapapun dan tidak ada dendam. "Dengan senang hati kalau sudah ya sudah, profesional," kata dia. (lutfi ahmad mauludin)"""
    classifier = NaiveBayesClassifier()
    result = classifier.classifier(text)
    pprint(result)

```
