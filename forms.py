from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length

class ArticleForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=200)])
    description = TextAreaField('Description', validators=[Length(max=500)])
    content = TextAreaField('Content', validators=[DataRequired()])
    category = SelectField('Category', choices=[
        ('General', 'General'),
        ('How-To', 'How-To'),
        ('Troubleshooting', 'Troubleshooting'),
        ('Other', 'Other')
    ])
    tags = StringField('Tags (comma-separated)')
