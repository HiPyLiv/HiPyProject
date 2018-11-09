const gulp        = require('gulp');
const browserSync = require('browser-sync').create();
const sass        = require('gulp-sass');
const jade        = require('gulp-jade');

// Compile Sass & Inject Into Browser
gulp.task('sass', function() {
    return gulp.src(['../docs/scss/*.scss'])
        .pipe(sass())
        .pipe(gulp.dest("../docs/css"))
        .pipe(browserSync.stream());
});

gulp.task('jade', function() {
    return gulp.src(["../docs/jade/*.jade"])
        .pipe(jade({pretty: true}))
        .pipe(gulp.dest("../docs"))
})


// Watch Sass & Serve
gulp.task('serve', ['sass', 'jade'], function() {
    browserSync.init({
        server: "./../docs"
    });

    gulp.watch(['../docs/scss/*.scss'], ['sass']);
    gulp.watch(['../docs/jade/*.jade'], ['jade']);
    gulp.watch("../docs/*.html").on('change', browserSync.reload);
});

// Default Task
gulp.task('default', ['serve']);
