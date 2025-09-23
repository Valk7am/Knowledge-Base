from flask import render_template, request, redirect, url_for, flash
from app import app, db
from models import Article, Tag
from forms import ArticleForm

# Home page: display all articles
@app.route('/')
def index():
    category_filter = request.args.get('category')
    tag_filter = request.args.get('tag')
    search_query = request.args.get('q')

    articles = Article.query

    if search_query:
        articles = articles.filter(
            Article.title.contains(search_query) | 
            Article.content.contains(search_query) |
            Article.description.contains(search_query)
        )
    if category_filter:
        articles = articles.filter_by(category=category_filter)
    if tag_filter:
        articles = articles.join(Article.tags).filter(Tag.name == tag_filter)

    articles = articles.order_by(Article.created_at.desc()).all()
    all_tags = Tag.query.all()
    categories = ['General', 'How-To', 'Troubleshooting', 'Other']

    return render_template('index.html', articles=articles, categories=categories, tags=all_tags)

# Create new article
@app.route('/create', methods=['GET', 'POST'])
def create_article():
    form = ArticleForm()
    if form.validate_on_submit():
        # Process tags
        tag_names = [t.strip() for t in form.tags.data.split(',') if t.strip()]
        tags = []
        for name in tag_names:
            tag = Tag.query.filter_by(name=name).first()
            if not tag:
                tag = Tag(name=name)
                db.session.add(tag)
            tags.append(tag)

        article = Article(
            title=form.title.data,
            description=form.description.data,
            content=form.content.data,
            category=form.category.data,
            tags=tags
        )
        db.session.add(article)
        db.session.commit()
        flash('Article created successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('create_article.html', form=form)

# View single article
@app.route('/article/<int:article_id>')
def article_detail(article_id):
    article = Article.query.get_or_404(article_id)
    return render_template('article_detail.html', article=article)
