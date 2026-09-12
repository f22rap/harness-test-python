# Harness Python検証サンプル

Harnessの検証用リポジトリ `f22rap/harness-test-python` に最初に配置するサンプルです。Pythonの標準ライブラリだけでテストできます。

## 構成

- `search.py`：文字列を検索する小さな処理。
- `test_search.py`：空入力、通常検索、Unicode文字列などを確認するテスト。
- `.gitignore`：Pythonの一時ファイルなどをGitへ含めない設定。

## テストする

このフォルダーで次のコマンドを実行します。Python 3.12以上を想定しています。

```text
python -m unittest discover -s . -p test_search.py -v
```

3件のテストが成功し、最後に `OK` と表示されれば、サンプルの基本動作を確認できています。

## 最初に確認すること

このサンプルは空入力の処理を実装済みです。最初の目的は、コードを読み取り、既存テストを実行して結果を記録できることの確認です。

後で修正機能を試す場合は、独立した検証用ブランチとIssueに、追加する振る舞いや再現可能な不具合を定義します。このサンプルのテスト成功だけでは、Harnessの隔離実行・承認・GitHub提出・CIの認定が完了したことにはなりません。

## 自動テスト（GitHub Actions）

`main` への更新と、`main` 向けPull Requestの作成・更新・再オープンで
`Python sample CI` が動きます。Python 3.12の1ジョブ、最長3分です。
Pull Requestでは提案された変更の先頭コミットを検査します。
3つの基本テストが揃い、失敗・スキップ・想定内失敗がないことを確認します。

公式Actionsはコミットで固定し、リポジトリへの権限は読み取りのみです。
外部パッケージの追加、キャッシュ、成果物のアップロード、秘密値は使用しません。
設定元は `.github/workflows/python-ci.yml` です。

GitHub Actionsの利用量はGitHub側で計上されます。3分の制限は1ジョブの
上限であり、月額料金の上限ではありません。GitHubの無料枠・予算を別途確認してください。
このCIの成功だけでは、HarnessのGitHub App接続・main保護・実運用認定は完了しません。
