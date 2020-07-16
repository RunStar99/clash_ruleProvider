wget https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanEasyPrivacy.list -O EasyPrivacy.yaml
python3 clash_modify.py
git add EasyPrivacy.yaml
git commit -m 'update EasyPrivacy'
git push origin master
