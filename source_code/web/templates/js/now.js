new Vue({
    el: '.bodys', //el用于指定当前Vue实例为哪个容器服务，值通常为选择器字符串。
    data: { //data中用于存储数据，数据供el所指定的容器去使用。
        course:{},
        courseName:'',
        role:'',
        member:'',
    },
    mounted: function(){
        // 将vue实例的方法绑定到window对象中去 
        window.del = this.del;
        window.join=this.join;
        this.course=JSON.parse(localStorage.getItem('nowCourse'));
    },
    methods:{
        openUrl:function(){
            window.location.href="./URL Page.html";
        },
        openSuvey:function(){
            window.location.href="./Create Survey.html";
        },
        openMaker:function(){
            window.location.href="./Team Maker.html";
        },
        openResult:function(){
            window.location.href="./Result History.html";
        },
        backs:function(){
            window.location.href="./menu.html"
        },
        backCS:function(){
            window.location.href="./Team Maker.html"
        },
        saveSurvey:function(){
            alert("Save successfully!");
            window.location.href="./instructor_log.html"
        },
        logout:function(){
            window.location.href="./index.html"
        },
        generateMaker:function(){
            var role=this.role;
            var member=this.member;
            if(role!=null && role!="" && member!=null && member!=""){
                alert("Generate success!!!");
                window.location.href="./Survey Result.html"
            }else{
                alert("The text box cannot be empty!");
            }
        },
        deleteHistory:function(){
            alert("Delete succeeded!");
            window.location.href="./Result History.html";
        }
    },
})