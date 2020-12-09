# 施肥設計のための簡単なプログラムです。

(1) 肥料銘柄、成分、価格をsehi.csvに保存

(2) 施肥面積と、N, P, K成分投入量(kg)をfield.csvに保存

(3) sehi.pyを実行

以下をクリックすると実行できます。（Googleアカウントが必要です。）
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1_w1bE-xnVIVaqFa-_Hwdf0-XYcXMU1HP?usp=sharing)


# アルゴリズム

n種類の肥料銘柄について、施肥要件を満たす最小コストの購入量組み合わせを探索するものです。
探索手法としてモンテカルロ法を用いています。
（そのうち
MIN : C_i x_i
Subject to : F_ij x_j - b_i > 0

としてシンプレックス法にしたいです。）


問題の定義：


MIN : C_i x_i　and  (F_ij x_j - b_i)(F_ij x_j - b_i) 

ここに、

C_i：肥料iの質量当り価格(kg/円)

x_i：肥料iの購入量(kg)

F_ij：肥料iの成分IDj(N=1, P=2, K=3)の成分含有率(kg/kg %)

b_i：肥料成分ID(N=1, P=2, K=3)ごとの目標投入量(kg)

x_iをモンテカルロ法により求めています。
だいたい30000回くらい乱数生成すればいい感じになります。









