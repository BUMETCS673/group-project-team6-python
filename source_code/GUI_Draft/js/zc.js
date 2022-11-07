new Vue({
    el: '.forms', //el用于指定当前Vue实例为哪个容器服务，值通常为选择器字符串。
    data: { //data中用于存储数据，数据供el所指定的容器去使用。
        email:'',
        psw:'',
        psw_repeat:'',
    },
    mounted: function(){
        // 将vue实例的方法绑定到window对象中去 
        window.register = this.register

    },
    methods:{
        register:function(){
            var that=this;
            // $.ajax({
            //     url:"./js/jsonTest.json",
            //     method:'GET',
            // }).then(function (res) {
                
            // });
            var email=this.email;
            var pwd=this.psw;
            var psw_repeat=this.psw_repeat;
            var data=JSON.parse(localStorage.getItem('userInfo'));
            //console.log(data);
            if(email!="" && email!=null && pwd!="" && pwd!=null && psw_repeat!="" && psw_repeat!=null && pwd==psw_repeat){
                if(data!=null){
                    var users=data.user;
                    users.splice(users.length,0,{"uname":email,"pwd":pwd});
                    data={
                        "user":users
                    };
                }else{
                    data={
                        "user":[{"uname":email,"pwd":pwd,}]
                    }
                }
                localStorage.setItem('userInfo',JSON.stringify(data));
                alert("Registration successful!");
                window.location.href="./index.html";
            }else if(pwd!=psw_repeat){
                alert("The two   must be the same!");
            }else{
                alert("The username or password cannot be empty!");
            }
        }
    },
})