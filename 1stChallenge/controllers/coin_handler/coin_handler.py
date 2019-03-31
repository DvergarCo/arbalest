ó
Mý \c           @   sO  d  Z  d d l m Z d d l Z d d l Z y e j d  Wn n Xe   Z e e j    Z	 e j
 d  Z d Z e j
 d  j d  Z d	   Z d
   Z e d d d g  e d d d g  e d d d g  e d d d g  e d d d g  e d d d g  e d d d g  x  e j e	  d k rJe   q+Wd S(   s   coin handler.iÿÿÿÿ(   t
   SupervisorNs   coin_handler.pyt   kedig      à?t   COINSt   childrenc         C   s?   t  j d d  t  j d  } | j d  } | j |   d  S(   Ni    s   ../../protos/coin.wbot   translation(   t   coinRoott   importMFNodet	   getMFNodet   getFieldt
   setSFVec3f(   t   post   coinR   (    (    s   coin_handler.pyt	   make_coin   s    c          C   s^  t  j d  j d  }  |  j   } | d k rR t  j d d d d d d d  n  t  j d d	 | d
 d
 d d d  xâ t t |   D]Î } |  j |  } | j   } t	 j   } t
 j t g  t | |  D] \ } } | | d ^ qÎ   } | t k  rd | f GH|  j |  d  S| j d  }	 |	 j   }
 |
 d d |
 d <|	 j |
  q Wd  S(   NR   R   i    i   t   VICTORYgffffffÖ?gÉ?iÿÿÿ s   COINS LEFT: %dg{®Gáz?g¹?i   t   toucht   rotationi   (   t
   supervisort
   getFromDefR   t   getCountt   setLabelt   reversedt   rangeR   t   getPositiont   playert   matht   sqrtt   sumt   zipt   ACCEPT_DISTANCEt   removeMFt   getSFRotationt   setSFRotation(   R   t   countt   idxR   R
   t
   player_post   at   bt   distt   rotationFieldt   angle(    (    s   coin_handler.pyt   update   s$    "#?g      ø?i    g      ø¿g      à¿(   t   __doc__t
   controllerR    R   t
   py_compilet   compileR   t   intt   getBasicTimeStept   timestepR   R   R   R   R   R   R(   t   step(    (    (    s   coin_handler.pyt   <module>   s.   			"