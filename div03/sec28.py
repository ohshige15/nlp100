"""
28. MediaWikiマークアップの除去
27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．
"""

import re
from div03.sec20 import get_wiki_text
from div03.sec25 import extract_basic_info
from div03.sec26 import remove_emphasis
from div03.sec27 import remove_internal_link

external_link_with_text_regex = re.compile(r"\[https?://[^ ]+? (.*?)\]")
external_link_without_text_regex = re.compile(r"\[(https?://[^ ]+?)\]")

file_link_regex = re.compile(r"\[\[ファイル:([^\|]*?)\|[^\|]*?\|[^\|]*?\]\]")

br_tag_regex = re.compile(r"<br ?/>")
ref_tag_1_regex = re.compile(r"<ref.*?/>")
ref_tag_2_regex = re.compile(r"<ref.*?>(.|\s)*?</ref>")

lang_template_regex = re.compile(r"{{lang\|.+?\|(.+?)}}")


def remove_external_link(text):
    text = external_link_with_text_regex.sub(r"\1", text)
    text = external_link_without_text_regex.sub(r"\1", text)
    return text


def remove_file_link(text):
    text = file_link_regex.sub(r"\1", text)
    return text


def remove_tag(text):
    text = br_tag_regex.sub("", text)
    text = ref_tag_1_regex.sub("", text)
    text = ref_tag_2_regex.sub("", text)
    return text


def remove_lang_template(text):
    text = lang_template_regex.sub(r"\1", text)
    return text


def remove_all_markup(text):
    text = remove_emphasis(text)
    text = remove_internal_link(text)
    text = remove_external_link(text)
    text = remove_file_link(text)
    text = remove_tag(text)
    text = remove_lang_template(text)
    return text


if __name__ == "__main__":
    import pprint
    uk_text = get_wiki_text("イギリス")
    result_dict = extract_basic_info(uk_text)
    result_dict = {k: remove_all_markup(v) for k, v in result_dict.items()}
    pprint.pprint(result_dict, width=1000)
