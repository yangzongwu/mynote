### inline
```html
<h2 style="color: blue;">CatPhotoApp</h2>
```
###  Style Elements
```html
<style>
  h2 {
    color: blue;
  }
</style>
<h2>CatPhotoApp</h2>
```
###  Class
```html
<style>
  .red-text {
    color: red;
  }
</style>
<h2 class="red-text">CatPhotoApp</h2>
<p class="red-text">view more</p>
```
###  Hex Code & RGB values
```html
body {
    color: #000000;
    background-color: rgb(255, 165, 0);
}
```
### Transparent
```html
h4{
    color:rgba(84, 40, 72,0.5)
}
```
### whole page
```html
body {
  background-color: black;
}
```


### Complementary ColorsPassed
red (#FF0000) and cyan (#00FFFF)  
green (#00FF00) and magenta (#FF00FF)  
blue (#0000FF) and yellow (#FFFF00)  
### Tertiary ColorsPassed
orange	#FF7F00  
cyan	#00FFFF  
raspberry	#FF007F  
### HSL
red	hsl(0, 100%, 50%)  
yellow	hsl(60, 100%, 50%)  
green	hsl(120, 100%, 50%)  
cyan	hsl(180, 100%, 50%)  
blue	hsl(240, 100%, 50%)  
magenta	hsl(300, 100%, 50%)  
### Gradual CSS Linear Gradient
background: linear-gradient(gradient_direction, color 1, color 2, color 3, ...);   
The first argument specifies the direction from which color transition starts - it can be stated as a degree, where 90deg makes a vertical gradient and 45deg is angled like a backslash.  
```html
<style>
  div {
    border-radius: 20px;
    width: 70%;
    height: 400px;
    margin: 50px auto;
    background: linear-gradient(35deg, #CCFFFF, #FFCCCC);
  }
</style>
<div></div>
```

```html
<style>
  div{
    border-radius: 20px;
    width: 70%;
    height: 400px;
    margin: auto;
    background: repeating-linear-gradient(
      45deg,
      yellow 0px,
      yellow 40px,
      black 40px,
      black 80px
    );
  }
</style>

<div></div>

```
