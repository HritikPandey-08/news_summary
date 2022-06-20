from newspaper import Article
from googletrans import Translator

url = "https://hindi.news18.com/news/uttar-pradesh/lucknow-yogi-adityanath-meets-governor-anandiben-patel-stakes-claim-to-form-government-in-the-state-nodark-4149546.html"


def translate_news(language_code):
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    translator = Translator()

    # Printing Article Title
    article_title = translator.translate(article.title, dest=language_code)
    print("Article Title:\n", article_title.text, "\n")

    # Printing Article content
    article_content = translator.translate(article.text, dest=language_code)
    print("Article Content: \n", article_content.text, "\n")

    # Printing Article Summary
    article_sum = translator.translate(article.summary, dest=language_code)
    print("Article Summary: \n", article_sum.text, "\n")

    # Printing Publish Date
    print("Article Publish Date: \n", article.publish_date, "\n")

    # Printing Article Top-Image Link
    print("Article Image link: \n", article.top_image, "\n")

    file1 = open("News_summary_File.txt", "w+",encoding='utf-8')
    file1.write("Title:\n")
    file1.write(article_title.text)
    file1.write("\n\nArticle Text:\n")
    file1.write(article_content.text)
    file1.write("\n\nArticle Summary:\n")
    file1.write(article_sum.text)
    file1.write("\n\nArticle Publish Date:\n")
    file1.write(str(article.publish_date))
    file1.write("\n\nArticle Image link:\n")
    file1.write(article.top_image)
    file1.close()


translate_news("hi")
