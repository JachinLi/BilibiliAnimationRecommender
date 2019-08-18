"""modify tables

Revision ID: 21538ad23e70
Revises: 
Create Date: 2019-06-30 16:30:27.860932

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '21538ad23e70'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('animation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('link', sa.String(length=100), nullable=True),
    sa.Column('is_finish', sa.Boolean(), nullable=True),
    sa.Column('media_id', sa.Integer(), nullable=True),
    sa.Column('follow', sa.String(length=20), nullable=True),
    sa.Column('play', sa.String(length=20), nullable=True),
    sa.Column('pub_date', sa.Integer(), nullable=True),
    sa.Column('pub_real_time', sa.Integer(), nullable=True),
    sa.Column('renewal_time', sa.Integer(), nullable=True),
    sa.Column('score', sa.Float(), nullable=True),
    sa.Column('season_id', sa.Integer(), nullable=True),
    sa.Column('title', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_animation_media_id'), 'animation', ['media_id'], unique=False)
    op.create_table('user_info',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('mid', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('sex', sa.String(length=10), nullable=True),
    sa.Column('sign', sa.Text(), nullable=True),
    sa.Column('rank', sa.Integer(), nullable=True),
    sa.Column('level', sa.Integer(), nullable=True),
    sa.Column('jointime', sa.Integer(), nullable=True),
    sa.Column('moral', sa.Integer(), nullable=True),
    sa.Column('silence', sa.Integer(), nullable=True),
    sa.Column('birthday', sa.String(length=20), nullable=True),
    sa.Column('coins', sa.Integer(), nullable=True),
    sa.Column('fans_badge', sa.Boolean(), nullable=True),
    sa.Column('role', sa.Integer(), nullable=True),
    sa.Column('title', sa.Text(), nullable=True),
    sa.Column('desc', sa.Text(), nullable=True),
    sa.Column('vip_type', sa.Integer(), nullable=True),
    sa.Column('vip_status', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_info_mid'), 'user_info', ['mid'], unique=False)
    op.create_table('animation_feature',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('media_id', sa.Integer(), nullable=True),
    sa.Column('tag_list', sa.Text(), nullable=True),
    sa.Column('review_times', sa.Integer(), nullable=True),
    sa.Column('character_voice_list', sa.Text(), nullable=True),
    sa.Column('character_staff_list', sa.Text(), nullable=True),
    sa.Column('short_comment_sum', sa.Integer(), nullable=True),
    sa.Column('long_comment_sum', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['media_id'], ['animation.media_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_stat',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('mid', sa.Integer(), nullable=True),
    sa.Column('following', sa.Integer(), nullable=True),
    sa.Column('whisper', sa.Integer(), nullable=True),
    sa.Column('black', sa.Integer(), nullable=True),
    sa.Column('follower', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['mid'], ['user_info.mid'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_upstat',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('mid', sa.Integer(), nullable=True),
    sa.Column('archive_view', sa.Integer(), nullable=True),
    sa.Column('article_view', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['mid'], ['user_info.mid'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_upstat')
    op.drop_table('user_stat')
    op.drop_table('animation_feature')
    op.drop_index(op.f('ix_user_info_mid'), table_name='user_info')
    op.drop_table('user_info')
    op.drop_index(op.f('ix_animation_media_id'), table_name='animation')
    op.drop_table('animation')
    # ### end Alembic commands ###
