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
![\begin{equation}
\Min \hspace{1cm} c_i x_i
\end{equation}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Bequation%7D%0A%5CMin+%5Chspace%7B1cm%7D+c_i+x_i%0A%5Cend%7Bequation%7D)

