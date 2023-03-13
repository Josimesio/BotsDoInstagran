from instapy import InstaPy
from instapy import smart_run

session = InstaPy(username='Seu instagram aqui', password='Sua senha Aqui')

with smart_run(session):
	session.set_do_follow(enabled = True, percentage = 100) #/*seguir os perfis*/
	session.set_do_like(enabled = True, percentage= 100) #/*dar like no perfil*/

	session.like_by_tags(['udemy'], amount=5) #/*hashtag que quero pesquisar e quantidade de post que quero olhar

	comentarios = ['Comentario 1 aqui', 'comentario 2 aqui']
	session.set_do_comment(enabled=True, percentage=95) #/*percentual de perfis seguidos com a hashtag*/
	session.set_comments(comentarios, media= 'Photo') #/*Onde vai fazer o comentario*/
	session.join_pods()