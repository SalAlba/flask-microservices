
run-app-user:
	cd user-services; \
	make run-app

run-app-order:
	cd order-services; \
	make run-app

run-app-product:
	cd product-services; \
	make run-app


run-all-apps:
	# make run-app-user
	# make run-app-product
	make run-app-order


run-all-apps-nohup:
	cd user-services; \
	make run-app-nohup; \
	cd ..; \
	cd product-services; \
	make run-app-nohup
	cd ..; \
	cd order-services; \
	make run-app-nohup;