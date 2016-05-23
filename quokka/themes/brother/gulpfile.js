
var gulp = require('gulp');
var rev = require('gulp-rev'); // 对文件名加MD5后缀
var revCollector = require('gulp-rev-collector'); // 模板路径替换
var debug = require('gulp-debug'); // DBEUG

gulp.task('concat', function() {                         
    gulp.src(['./static/css/*.css']) 
        // 文件名加MD5后缀  
        .pipe(rev())        
        // 输出文件本地                                   
        .pipe(gulp.dest('./static/css'))                             
        // 生成一个rev-manifest.json
        .pipe(rev.manifest())                                  
        // 将 rev-manifest.json 保存到 rev 目录内
        .pipe(gulp.dest('./rev'));                              
});

gulp.task('rev', function() {
    gulp.src(['./rev/*.json', './templates/*.html'])  
        // 替换模板中文件名
        .pipe(revCollector())
        // 输出文件
        .pipe(gulp.dest('./templates/')).debug();
});

gulp.task('default', ['concat', 'rev']);