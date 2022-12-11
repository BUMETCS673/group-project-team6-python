new Vue({
    el: '.row', //el用于指定当前Vue实例为哪个容器服务，值通常为选择器字符串。
    data: { //data中用于存储数据，数据供el所指定的容器去使用。
        courses:[],
        courseName:'',
    },
    mounted: function(){
        // 将vue实例的方法绑定到window对象中去 
        window.del = this.del;
        window.join=this.join;
        var courses=JSON.parse(localStorage.getItem('courses'));
        if(courses!=null){
            this.courses=courses;
        }else{
            courses=[
                {
                    "name":"CS673",
                    "title":"SOFTWARE ENGINEERING",
                    "show":true
                  },{
                    "name":"CS683",
                    "title":"Mobile Application Development with Android",
                    "show":true
                  },{
                    "name":"CS575",
                    "title":"Operating Systems",
                    "show":true
                  }
            ];
            this.courses=courses;
            localStorage.setItem('courses',JSON.stringify(courses));
        }
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
        },

        del:function(name){
            var data=JSON.parse(localStorage.getItem('courses'));
            for(var i=0;i<data.length;i++){
                if(data[i].name==name){
                    data[i].show=false;
                }
            }
            alert("Delete the success");
            localStorage.setItem('courses',JSON.stringify(data));
            window.location.href="./instructor_log.html";
        },
        add:function(){
            var courseName=this.courseName;
            var title = this.title
            if(courseName!=""){
                var data=JSON.parse(localStorage.getItem('courses'));
                data.splice(data.length,0,{"name":courseName,"title":title,"show":true});
                localStorage.setItem('courses',JSON.stringify(data));
                alert("New success");
                window.location.href="./instructor_log.html";
            }else{
                alert("course name is not null!");
            }
            
        },
        join:function(name){
            var data=JSON.parse(localStorage.getItem('courses'));
            for(var i=0;i<data.length;i++){
                if(data[i].name==name){
                    localStorage.setItem('nowCourse',JSON.stringify(data[i]));
                    window.location.href="./menu.html";
                    break;
                }
            }
        }
    },
})