# CreditCalculatorWEBapp
WEBapp version.
CreditCalculator<https://github.com/TT375S/CreditCalculator.git>のWebアプリケーション版です。
Calculatorの綴りをどちらも間違えていましたが一部は修正しました。

大学の成績照会のページ<https://iaidp.ia.waseda.jp/idp/profile/SAML2/Redirect/SSO;jsessionid=C1C4CD947A9D5    2B605515638EA7D720C?executio    n=e1s1>から、どの群の科目の単位をどれだけとったかと、GPAを算出するプログ>    ラムです。  
(残念ながら、特定の一つの大学しか対応していません。)  

##前提となるもの
Python2.xiが使えるサーバさえあれば、特に用意するものはありません。  

##使い方
適当なフォルダで、  
`$ git clone https://github.com/TT375S/CreditCalculatorWEBapp.git`   
としてクローンします。  
次に、ファイルのあるディレクトリに移動します。  
`$ cd CreditCalculator/files`   
実行します。(8080ポートを指定していますが、開いているポートを指定してください。)  
`$python  m CGIHTTPServer 8080`  
  
CGIサーバが立ちます。http://(IPアドレスorドメイン):8080/にアクセスしてください。  
後は、大学の成績照会ページ<https://my.waseda.jp/login/login>に行って、成績が表示されているページのHTMLソ>    ースコードをコピーして、貼り付けて送信ボタンを押します。。   
 
##出力例  
	   評価別の数(＊は未評価)   
	A 17
	C 2
	B 13
	G 0
	F 0
	H 0
	A+ 3
	＊ 11

	   成績計算   
	scoreSum 91
	class 46
	finishedClass 35
	GPA 2.6
	</body></html>
