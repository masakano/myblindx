import flet as ft

def main(page: ft.Page):
    # クリップボードの内容を取得する関数
    def get_clipboard_content(e):
        # クリップボードからテキストを取得
        content = page.get_clipboard()
        # テキストをラベルに表示
        output_label.value = f"クリップボードの内容: {content}"
        page.update()

    # ボタンとラベルを作成
    output_label = ft.Text(value="クリップボードの内容がここに表示されます")
    get_clipboard_button = ft.ElevatedButton(
        text="クリップボードの内容を取得",
        on_click=get_clipboard_content
    )

    # 要素をページに追加
    page.add(get_clipboard_button, output_label)

# アプリケーションを実行
ft.app(target=main)
