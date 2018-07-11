---
layout: default
title: contacto
permalink: /contact/
---
<style type="text/css" media="screen">
 input, textarea{
    border: 3px solid #009999;
    width: 500px;
    padding: 10px;
  }

  
 [type="submit"]{
    background: #008080;
    color: white;
    font-size: 18px;
    width: 525px;
  }

  textarea{
    height: 10em;
  }

  label{
    display: block;
    margin-bottom: 28px;
  }

  span_form{display: block;}


</style>

<form action="https://formspree.io/florrr1997@gmail.com"
      method="POST">
    <input type="hidden" name="_subject" value="{{site.title}}" />
    <input type="hidden" name="_cc" value="{{site.email1}}" />
    <label><span_form>Nombre</span_form>
    <input type="text" name="name"></label>

    <label><span_form>Email</span_form>
    <input type="email" name="_replyto"></label>

    <textarea name="message"></textarea>
    <input type="submit" value="Enviar">

</form>