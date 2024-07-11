# life_game

## 使用言語：<img src="https://img.shields.io/badge/-Python-3776AB.svg?logo=python&style=social"></br>

## 開発概要
<p>
ライフゲームを少し改変させ、対戦型のライフゲームをコード制御で遊ぶ。
</p>

# developの使い方。
<p>
develop内で書くシステムごとにブランチを切り、各々が開発を進めていく。</br>
システムごとにブランチを切るときは、issueに挙げてね♡
</p>

# 開発環境設定について
<p>
せっかくなので共同開発っぽくvenvの使用を推奨する。</br>
<em>以下環境開発手順</em>
<ol>
<li>
開発用のファイルの根本に仮想環境用のファイルを作成する。
</li>
<p>
例えば→　C:\programings\make_grassy　を作成
</p>
<li>
仮想環境用ファイルにvenvのファイルを作成する。
</li>
<p>
例）
<code>PS C:\programing> python -m venv venv</code></br>
右端のvenvはファイル名になるので、自由に書き換えてよし
</p>

<li>
作成したvenvファイルの直下に、git cloneでgitのファイルを受け取る。
</li></br>

<p>
ファイルのネスト例
<pre><code>
-C
    -programing
        >some_file
        >anything_file
        -make_grassy
            -vemv
                >Include
                >Lib
                <strong>-life_game</strong>
                    communicate.txt
                    EDTest.py
                    README.md
                    requirements.txt
                >Scripts
                pyvemv.cfg
        >other_file
</code></pre>
<li>
仮想環境の起動
</li>
<p>
以下の実行場所はvenvの親ファイル(自分の場合はC:/programingで実行)
<code>PS C:\programing\make_grassy> .\venv\Scripts\activate</code>
</p>
<p>
ここなんかうまくいかないこと多いから。以下手順で解消されるかも</br>
VScord内上部の表示　→　コマンドパレット　→　「setting」で検索　→　基本設定：ユーザー設定</br>
で<em>setting.json</em>を開く</br></br>
ファイル内下部に</br>
<pre><code>
"terminal.integrated.env.windows": {
        "PSExecutionPolicyPreference": "RemoteSigned"
    }    
</code></pre></br>
を入力する。<strong>VScordの再起動</strong>をしたら完了。もう一度トライ
</p>

<li>
仮想環境に入ったかを確認。</br>
確認方法</br>
<code>(venv) PS C:\OOOOOOO\OOOOOO</code></br>
になってたらおｋ。
</li>
</br></br>
<h2>ここまでで仮想環境のセットアップ完了！！！！おめでとう！！！！！！！！！！</h2>
</br></br>

<li>
pipで共有されたライブラリのインストール
</li>
<p>
仮想環境起動後のvenv内で以下実行するだけで終わり。</br>
<code>(venv) PS C:\programing\make_grassy\venv> pip install -r requirements.txt</code>
</p>

<li>
コードの実行テスト
</li>
<p>
＄ C:\~~~~~~~\life_game　に入り、python EDTest.py　で実行する。
</p>

<li>
仮想マシンの停止
</li>
<p>これだけで終わるよ。</br>
<code>deactivate</code>
</p>
</ol>


</p>
