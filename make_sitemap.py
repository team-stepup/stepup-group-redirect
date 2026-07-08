# -*- coding: utf-8 -*-
"""Google検索に残っている旧URLを列挙した sitemap-old.xml を生成する。
再クロールを促し、転送/404 を早く認識させて恒久de-indexを加速するのが目的。
"""
from urllib.parse import quote

PATHS = [
    "/",
    "/topics/",
    "/privacypolicy/",
    "/otherjob/",
    "/honyaku/",
    "/iwatajob/",
    "/contact/",
    "/contact/form/",
    "/outline/",
    "/hamamatsujob/",
    "/job/",
    "/fukuroijob/",
    "/staff/",
    "/kakegawajob/",
    "/outline/コンセプト/",
    "/outline/会社概要/",
    "/privacypolicy/プライバシーポリシー/",
    "/iwatajob/事務系/",
    "/iwatajob/販売系/",
    "/otherjob/生産系-4/",
    "/fukuroijob/生産系-3/",
    "/hamamatsujob/生産系-2/",
    "/有料職業紹介事業の概要/",
    "/労働者派遣事業制度の概要/",
    "/staff/人材をお探しの方/",
    "/honyaku/ポルトガル語専門　通訳・翻訳について/",
    "/topics/マージン率等情報を更新しました-3/",
    "/topics/有料職業紹介事業の概要を追加しました/",
    "/topics/web面接の利用が可能になりました。/",
    "/topics/掛川市生産系求人情報を追加しました。/",
    "/topics/磐田市生産系求人情報を追加しました。/",
    "/topics/袋井市生産系求人情報を追加しました。-2/",
    "/topics/磐田市の生産系求人情報を掲載しました。-2/",
    "/topics/磐田市、掛川市の生産系求人情報を追加しました/",
]

urls = []
for p in PATHS:
    enc = quote(p, safe="/-.")
    urls.append(f"  <url><loc>https://www.stepup-group.jp{enc}</loc></url>")
    urls.append(f"  <url><loc>https://stepup-group.jp{enc}</loc></url>")

xml = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + "\n".join(urls)
    + "\n</urlset>\n"
)

with open("sitemap-old.xml", "w", encoding="utf-8") as f:
    f.write(xml)
print(f"OK {len(PATHS)} paths x2 hosts = {len(urls)} URLs")
