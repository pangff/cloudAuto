#echo "==install env==="
#cd ~/git
#git clone https://github.com/creationix/nvm.git
#source ~/git/nvm/nvm.sh
#NVM_NODEJS_ORG_MIRROR=https://npm.taobao.org/mirrors/node nvm install 7.5.0
#npm --registry=https://registry.npm.taobao.org install cnpm -g
#cd ..
cd ~/code/cloudAuto/simple-restify
npm install;
npm install pm2@latest -g
echo "==start server==="
node ~/code/cloudAuto/simple-restify/index.js &
\n
echo "==done==="