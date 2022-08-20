# day one

sudo apt-get install yum

Elk stack
https://github.com/soumilshah1995/AWS-Elastic-Search-and-kibana-Deploy/blob/master/README.md#step6install-plugins

Py3 kuruldu

Pip kurulumu
Yum install python-pip

Jupyter kurulumu
https://thelinuxgurus.com/simple-guide-to-install-jupyter-notebook-on-linux/
Alınan hata ve çözümü:
https://stackoverflow.com/questions/50374710/oserror-errno-99-cannot-assign-requested-address
jupyter notebook --ip=127.0.0.1 --port=8888
Jupyter password:
112233

Jupyter py3 kuruldu
https://stackoverflow.com/questions/28831854/how-do-i-add-python3-kernel-to-jupyter-ipython

Elastic search pip kuruldu
pip install elasticsearch
Pandas pip kuruldu
Pip install pandas

# day two

Kibana apache luciene den gelir. Apache luciene kodları els

Reldb - ElasticSearch
Database-index
Table-type
Row-document
Column-fields
Schema-mapping

---

Kaggle: veriler burada

Elastic status check
sudo service elasticsearch.service status -l

Elastic restart
sudo service elasticsearch.service restart

systemctl daemon-reload

Elastic 1.7 to 7.6

Yeni tutorial ile elk kurulum denemeleri
https://www.elastic.co/blog/running-elasticsearch-on-aws

Connect es cloud
https://www.elastic.co/guide/en/cloud/current/ec-getting-started-python.html#ec_ingest_data_2

# day three

Gün notları: elastic co üzerinde oluşturulan index görüntülendi

Elasticsearch language clients are only backwards compatible with default distributions and without guarantees made.

# 24 March 2022

Exception has occurred: ConnectionError
ConnectionError(<urllib3.connection.HTTPConnection object at 0x0000022936915F30>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it) caused by: NewConnectionError(<urllib3.connection.HTTPConnection object at 0x0000022936915F30>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it)

Neden: doc_type`ın eşleştiği bir document olmadığından bu hatayı verir

es.index(index="my-index", doc_type="\_doc", body={"any": "data", "timestamp": "datetime.now()"})

Elastic Search error [WinError 10061] No connection could be made because the target machine actively refused it)

Kaynak <https://stackoverflow.com/questions/65704216/elastic-search-error-winerror-10061-no-connection-could-be-made-because-the-ta>

Neden:
1-doğru versiyonlar kullanılmamaktadır
2-doğru versioynlar kullanılsa bile import edilen kütüphaneler doğru şekilde okunamamaktadır

401 Unauthorized
Neden:
Api authantication bilgileri yanlış girilmiştir.

# 21 May:

## index

https://testingelastic-72675f.kb.us-central1.gcp.cloud.es.io:9243/app/management/data/index_management/indices

## dataview

Pyscript elk hata çözümü

https://stackoverflow.com/questions/72490512/pyscript-elastic-searchelk-enterprise-connection-error
