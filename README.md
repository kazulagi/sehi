# 施肥設計のための簡単なプログラムです。

(1) 肥料銘柄、成分、価格をsehi.csvに保存
(2) 施肥面積と、N, P, K成分投入量(kg)をfield.csvに保存
(3) sehi.pyを実行

以下をクリックしてください。（Googleアカウントが必要です。）
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1_w1bE-xnVIVaqFa-_Hwdf0-XYcXMU1HP?usp=sharing)


# アルゴリズム

n種類の肥料銘柄について、施肥要件を満たす最小コストの組み合わせを探索するものです。
探索手法としてモンテカルロ法を用いています。

問題の定義：


< img src="https://render.githubusercontent.com/render/math?math= min: c_i " >