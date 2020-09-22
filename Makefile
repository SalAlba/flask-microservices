
run-all-apps:
	cd user-services; \
	make run-app


run-all-apps-nohup:
	clean; \
	clear;
	nohup python3 run_ann.py &