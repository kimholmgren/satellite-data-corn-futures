wget 'https://earthengine.googleapis.com/api/download?docid=5eed228f79cc98a630ee01bd7de92117&token=e5a579e8acdbcc8f306b269a05166c32' -O download2000.zip
unzip download2000.zip
mv *.nd.tif 2000.tif

wget 'https://earthengine.googleapis.com/api/download?docid=bbb8140703156e64d133a269265cd892&token=6ffdb6c51a94eed21648e28d89b459f1' -O download2001.zip
unzip download2001.zip
mv *.nd.tif 2001.tif

wget 'https://earthengine.googleapis.com/api/download?docid=eb7ad0b019784d4c9256eaf1cd487dc4&token=d8d15d9bf699b487d58eb85a5540635a' -O download2002.zip
unzip download2002.zip
mv *.nd.tif 2002.tif

wget 'https://earthengine.googleapis.com/api/download?docid=724d2d5f094d63941b4d8789bfe38b01&token=6a5f10f6bea3e644a3bb370030afad81' -O download2003.zip
unzip download2003.zip
mv *.nd.tif 2003.tif

wget 'https://earthengine.googleapis.com/api/download?docid=f7f9c868abc3a4362ee9705afbbb49d9&token=e968fc17ddb4b62ebbdd095c81ea5a48' -O download2004.zip
unzip download2004.zip
mv *.nd.tif 2004.tif

wget 'https://earthengine.googleapis.com/api/download?docid=612b268c11afb3ab3806237cf857e478&token=60e36d9d9c02053654169b5921d038c0' -O download2005.zip
unzip download2005.zip
mv *.nd.tif 2005.tif

wget 'https://earthengine.googleapis.com/api/download?docid=edfd6cf93c044fefb4144bc3a483981d&token=8337e6ecef9ed35fd850389fa0e80952' -O download2006.zip
unzip download2006.zip
mv *.nd.tif 2006.tif

wget 'https://earthengine.googleapis.com/api/download?docid=6c0fafd7af631e959ed7db4439465da0&token=ba4dbaf3de84337bc34aa6c658c1da63' -O download2007.zip
unzip download2007.zip
mv *.nd.tif 2007.tif

wget 'https://earthengine.googleapis.com/api/download?docid=80753f3b351905dfd23a349c3bc42108&token=9847537b9ca482c3f153af93feb2d83e' -O download2008.zip
unzip download2008.zip
mv *.nd.tif 2008.tif

wget 'https://earthengine.googleapis.com/api/download?docid=1c9793412672f93bf328f93e30b57a78&token=371d71aadcb327f1e0ebe68d6862f42e' -O download2009.zip
unzip download2009.zip
mv *.nd.tif 2009.tif

wget 'https://earthengine.googleapis.com/api/download?docid=a5314453cc4e8c36a98133c82f0febb6&token=3e26d9f229f5a75f66e2f725a0988cb8' -O download2010.zip
unzip download2010.zip
mv *.nd.tif 2010.tif

wget 'https://earthengine.googleapis.com/api/download?docid=4a992df499e3ebb7818587d5ce0f63bc&token=4a4caaeebf7ae2c6e864fd137d8ea920' -O download2011.zip
unzip download2011.zip
mv *.nd.tif 2011.tif

wget 'https://earthengine.googleapis.com/api/download?docid=5ccf2256c8f6843d98e2bc2841e3ebf4&token=83c5a531d346e88fe0a1c0948a8ae1bb' -O download2012.zip
unzip download2012.zip
mv *.nd.tif 2012.tif

wget 'https://earthengine.googleapis.com/api/download?docid=44a298efa09ca4e05b2d7cb89b49a2f9&token=85990ce9ce9541661a9e64727e486854' -O download2013.zip
unzip download2013.zip
mv *.nd.tif 2013.tif

wget 'https://earthengine.googleapis.com/api/download?docid=a721abebfc4189eabef60b551019f616&token=88dfdd7c3d8f62046ab215348da30c29' -O download2014.zip
unzip download2014.zip
mv *.nd.tif 2014.tif

wget 'https://earthengine.googleapis.com/api/download?docid=a012ba4d4e98efe5aafe977193dad015&token=d962fe940ea487c0b81054c128663b19' -O download2015.zip
unzip download2015.zip
mv *.nd.tif 2015.tif

for file in download*; do rm $file; done
rm *tfw