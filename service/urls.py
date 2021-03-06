from django.conf.urls import url
import views

urlpatterns = [
	
	# #
	#  URL FOR USER ACTIONS
	#  1. auth/user/signup - FOR USER REGISTRATION
	#  2. auth/user/signin - FOR USER SIGNIN AND GENERATE TOKEN
	#  3. user/upload - FOR GETTING ALL UPLOADS BY USER
	# #

	## User Register URI
	url(r'^auth/user/signup$', views.ServiceView.as_view('userSignup', method=['POST']) ),

	## User Login URI
	url(r'^auth/user/signin$', views.ServiceView.as_view('userSignIn', method=['POST']) ),

	## Get All Uploads By User URI
	url(r'^user/uploads$', views.ServiceView.as_view('listUserUploads', method=['GET']) ),
	

	# #
	#  URL FOR UPLOAD ACTIONS
	#  1. service/image - POST - FOR UPLOADING IMAGE
	#  2. service/image - GET - FOR VIWEING IMAGE USING LINK
	#  3. service/image/upload-id - FOR UPDATING IMAGE
	# #

	## URI for Uploading an image
	url(r'^serve/image$', views.ServiceView.as_view('uploadImage', method=['POST']) ),

	# URI for updating/deleting an image
	url(r'^serve/image/(?P<upload_id>[a-zA-Z0-9\-]+)$', views.ServiceView.as_view('updateImage', method=['PATCH', 'DELETE']) ),
	
	## URI for Viewing an image by image-name
	url(r'^serve/image/(?P<filename>[\w.-]+)$', views.ServiceView.as_view('viewImage', method=['GET']) ),

]