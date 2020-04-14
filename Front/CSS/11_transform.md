### Change the Size of an Element
```html
p {
  transform: scale(2);
}
```
```html
<style>
  div{
    width: 70%;
    height: 100px;
    margin:  50px auto;
    background: linear-gradient(53deg,#ccfffc,#ffcccf);
  }
  div:hover{
    transform:scale(1.1);
  }
</style>
<div></div>
```
### Change the degree of an Element
skewX(), which skews the selected element along its X (horizontal) axis by a given degree.
```html
#bottom {
    background-color: blue;
    transform: skewX(24deg);
}
```
skewY() property skews an element along the Y (vertical) axis
```html
#top {
    background-color: red;
    transform:skewY(-10deg);
  }
```
