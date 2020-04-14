One feature of Sass that's different than CSS is it uses variables. They are declared and set to store data, similar to JavaScript.

In JavaScript, variables are defined using the let and const keywords. In Sass, variables start with a $ followed by the variable name.

Here are a couple examples:

```sass
<style type='text/sass'>
  $text-color:red;
  .blog-post, h2 {
    color: $text-color;
  }
</style>
```
