new Vue({
    el: '.header', //el用于指定当前Vue实例为哪个容器服务，值通常为选择器字符串。
    data: { //data中用于存储数据，数据供el所指定的容器去使用。
        uname:'',
        psw:'',
    },
    mounted: function(){
        // 将vue实例的方法绑定到window对象中去 
        window.login = this.login

    },
    methods:{
        login:function(){
            var that=this;
            //alert(this.uname);
            // $.ajax({
            //     url:"./js/jsonTest.json",
            //     method:'GET',
            // }).then(function (res) {
                
            // });
            var uname=this.uname;
            var pwd=this.psw;
            if(uname!="" && uname!=null && pwd!="" && pwd!=null){
                var userInfo=JSON.parse(localStorage.getItem("userInfo"));
                var bl=false;
                for(var i=0;i<userInfo.user.length;i++){
                    if(userInfo.user[i].uname==uname && userInfo.user[i].pwd==pwd){
                        alert("Login successful!");
                        bl=true;
                        break;
                    }
                }
                if(!bl){
                    alert("Incorrect password or user name!");
                }else{
                    window.location.href="./instructor_log.html"; 
                }
                
            }else{
                alert("The username or password cannot be empty!");
            }
        }
    },
})