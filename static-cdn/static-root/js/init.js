/*
 * Copyright (c) 2021 Frenify
 * Author: Frenify
 * This file is made for CURRENT TEMPLATE
*/

window.addEventListener("load", function(){
	"use strict";
	jQuery('body').addClass('preloader_loaded');
});


(function($){
  "use strict";
  
  
	var Industify = {
		
		
		/* collect all functions for next initialization */
		init: function(){
			
			/* Set background image from data attribute */
			Industify.BgImg();
			
			/* Change image into SVG */
			Industify.imgToSVG();
			
			/* Alpha Slider */
			Industify.alphaSlider();
			
			/* About Section Animation: used parallax JS */
			Industify.parallax();
			
			/* Owl Carousel for Service Query */
			Industify.serviceQueryCarousel();
			
			/* To top button */
			Industify.totop();
			
			/* Language box opener */
			Industify.languageOpener();
			
			/* Mobile menu opener (hamburger) */
			Industify.mobileMenuOpener();
			
			/* Mobile submenu opener */
			Industify.mobileSubmenuOpener();
			
			/* Toll free triangle calculation */
			Industify.triangleCalc();
			
			/* Language box position recalculation */
			Industify.languageCalc();
			
			/* Support Block Triangle calculation */
			Industify.supportBlockBgCalc();
			
			/* Light Gallery */
			Industify.lightGallery();
			
			/* Isotope Masonry */
			Industify.isotope();
			
			/* Kenburnsy Slider */
			Industify.kenburnsy();
			
			/* Magnific popup for youtube */
			Industify.popupYoutube();
			
			/* Spacing */
			Industify.spacer();
			
			/* Counter */
			Industify.counter();
			
			/* Five Stars calculation */
			Industify.fiveStars();
			
			/* Testimonial Slider with rating */
			Industify.reviewSlider();
			
			/* Portfolio Elegant List calculation */
			Industify.reCalcProjectElegant();
			
			/* Estimate Widget calculation */
			Industify.estimateWidgetCalc();
			
			/* Blog Page Shape calculation */
			Industify.blogShapeCalc();
			
			/* Contact Form */
			Industify.contactForm();
			
			/* Justified Images for Portfolio Single */
			Industify.justified();
			
			/* Portfolio Page Filter */
			Industify.portfolioFilter();
		},
		
		/* include html and run call collected function (which includes all functions) */
		getIncludedHTML: function(){
			var xhttp;
			var getHTML		= $('[data-html]'),
				count		= getHTML.length,
				i			= 0;
			getHTML.each(function(){
				var element	= $(this);
				var file 	= element.data("html");
				if (file) {
					/* make an HTTP request using the attribute value as the file name: */
					xhttp = new XMLHttpRequest();
					xhttp.onreadystatechange = function() {
						if (this.readyState === 4) {
							if (this.status === 200) {
								element.before(this.responseText);
								
								/* Only for random service */
								var attr = element.attr('data-index');
								if(typeof attr !== 'undefined' && attr !== false){
									var serviceIndex	= element.data('index');
									var serviceCount	= element.data('count');
									var services 		= element.siblings('.industify_fn_random_services');
									if(services.length){
										var children	= services.find('li');
										children.addClass('disable');
										var array		= Array.from({length:children.length},(v,k)=>k+1);
										var index 		= array.indexOf(serviceIndex);
										if (index > -1) {
											array.splice(index, 1);
										}
										var shuffled 	= array.sort(function(){return 0.5 - Math.random();});

										var selected	= shuffled.slice(0,serviceCount);
										$.each(selected,function(a,b){
											children.eq(b-1).removeClass('disable');
										});
										children.filter('.disable').remove();
									}
								}
								/***************************/
								
								element.remove();
								i++;if(i===count){Industify.init();}
							}
						}
					};
				  	xhttp.open("GET", file);
				  	xhttp.send();
				}
			});
			if(!count){
				Industify.init();
			}
		},
		
		portfolioFilter: function(){
			var filterB = $('.portfolio_list .filter');
			var mainBtn = $('.portfolio_list .filter > a');
			var filter	= $('.portfolio_list .fn_filter');
			var btns 	= $('.portfolio_list .fn_filter a');
			var spinner	= $('.portfolio_list .filter span.spinner');
			var listIn	= $('.industify_fn_portfolio_page .portfolio_list_in');

			var $grid = $('.industify_fn_portfolio_list').isotope({});
			$(window).on('click',function() {
				filter.removeClass('opened');
				filterB.removeClass('opened');
			});

			mainBtn.on('click',function(event){
				event.stopPropagation();
				if(filter.hasClass('opened')){
					filter.removeClass('opened');
					filterB.removeClass('opened');
				}else{
					filter.addClass('opened');
					filterB.addClass('opened');
				}
				return false;
			});
			btns.on('click',function(){
				var element = $(this);
				var ID 		= element.data('filter');
				var name 	= element.text();
				listIn.addClass('active');
				spinner.addClass('active');
				btns.removeClass('active');
				element.addClass('active');
				mainBtn.html(name);
				filter.removeClass('opened');
				filterB.removeClass('opened');
				
				Industify.doAjaxCall(ID,$grid,element,spinner);
				
				return false;
			});
		},
		
		doAjaxCall: function(ID,$grid,element,spinner){
			setTimeout(function(){
				$grid.isotope({ filter: ID });
				element.removeClass('active');
				spinner.removeClass('active');
			},500);
		},
		
		justified: function(){
			var justified = $(".fn_cs_justified");
			justified.each(function(){
				var element 	= $(this);
				var justHeight	= element.attr('data-height');
				var justGutter	= element.attr('data-gutter');
				if(typeof(justHeight) !== 'undefined' && typeof(justGutter) !== 'undefined'){
					if(justHeight !== ''){justHeight = justHeight;}
					if(justGutter !== ''){justGutter = justGutter;}
				}else{justHeight = 300;justGutter = 10;}
				element.parent().css({padding:justGutter+'px'});
				if($().justifiedGallery){
					element.justifiedGallery({
						rowHeight : justHeight,
						lastRow : 'nojustify',
						margins : justGutter,
						refreshTime: 500,
						refreshSensitivity: 0,
						maxRowHeight: null,
						border: 0,
						captions: false,
						randomize: false
					});
				}
			});	
		},
		
		
		blogShapeCalc: function(){
			var post = $('.industify_fn_postlist .post');
			if(post.length){
				post.each(function(){
					var el 		= $(this);
					var width	= Math.floor(el.width() - 100);
					var shape	= el.find('.shape2');
					if(width > 0){
						if(shape.length){
							shape.css({borderLeftWidth:width + 'px'});
						}
					}
				});
			}	
		},
		
		estimateWidgetCalc: function(){
			var est = $('.industify_fn_widget_estimate');
			est.each(function(){
				var el = $(this);
				var h1 = el.find('.helper1');
				var h2 = el.find('.helper2');
				var h3 = el.find('.helper3');
				var h4 = el.find('.helper4');
				var h5 = el.find('.helper5');
				var h6 = el.find('.helper6');
				var eW = el.outerWidth();
				var w1 = Math.floor((eW * 80) / 300);
				var w2 = eW-w1;
				var e1 = Math.floor((w1 * 55) / 80);
				h1.css({borderLeftWidth:w1+'px',borderTopWidth:e1+'px'});
				h2.css({borderRightWidth:w2+'px',borderTopWidth:e1+'px'});
				h3.css({borderLeftWidth:w1+'px',borderTopWidth:w1+'px'});
				h4.css({borderRightWidth:w2+'px',borderTopWidth:w1+'px'});
				h5.css({borderLeftWidth:w1+'px',borderTopWidth:w1+'px'});
				h6.css({borderRightWidth:w2+'px',borderTopWidth:w1+'px'});
			});
		},
		
		reCalcProjectElegant: function(){
			$('.fn_cs_project_elegant_list .right_part').each(function(){
				var element 	= $(this),
					height		= element.height(),
					width		= element.width(),
					ratio		= 300/420,
					imageHeight	= width*ratio,
					output		= height-(imageHeight*2);
				element.find('.item').eq(0).find('.title_holder').css({height: output + 'px',bottom: '-' + output + 'px'});
			});
		},
		
		fiveStars: function(){
			$('.fn_cs_review__stars').each(function(){
				var element		= $(this);
				var stars		= element.data('stars');
				var width		= stars * (100/5) + 1;
				var Xpos		= 100 - width;
				element.find('.rating_absolute').css({width:width+'px'});
				element.find('.rating_relative').css({width:Xpos+'px'});
				element.find('.rating_relative div').css({transform:'translateX(-'+width+'px)'});
			});
		},
		
		
		reviewSlider: function(){
			$('.fn_cs_personal_reviews .r_list').each(function(){
				var element 	= $(this);
				var container 	= element.find('.swiper-container');
				var mySwiper 	= new Swiper (container, {
					loop: true,
					slidesPerView: 3,
					spaceBetween: 70,
					speed: 1000,
					loopAdditionalSlides: 10,
					autoplay: {
						delay: 70000,
						disableOnInteraction: false
					},
					on: {
						init: function(){
							element.closest('.fn_cs_personal_reviews').addClass('ready');
						},
						autoplayStop: function(){
							mySwiper.autoplay.start();
						},
						slideChange: function () {
							Industify.imgToSVG();
						},
					},
					pagination: {
						el: '.fn_cs_swiper__progress',
						type: 'custom', // progressbar
						renderCustom: function (swiper,current,total) {

							// opacity 
							var index 		= current - 1;
							var activeSlide = container.find('.swiper-slide[data-swiper-slide-index="'+index+'"]');
							container.find('.r_item').removeClass('fn_vision');
							activeSlide.find('.r_item').addClass('fn_vision');
							activeSlide.next().find('.r_item').addClass('fn_vision');
							activeSlide.next().next().find('.r_item').addClass('fn_vision');



							// progress animation
							var scale,translateX;
							var progressDOM	= container.find('.fn_cs_swiper__progress');
							if(progressDOM.find('.all span').length){
								if(progressDOM.hasClass('fill')){
									translateX 	= '0px';
									scale		= parseInt((current/total)*100)/100;
								}else{
									scale 		= parseInt((1/total)*100)/100;
									translateX 	= (current-1) * parseInt((100/total)*100)/100 + 'px';
								}
								progressDOM.find('.all span').css({transform:'translate3d('+translateX+',0px,0px) scaleX('+scale+') scaleY(1)'});
								if(current<10){current = '0' + current;}
								if(total<10){total = '0' + total;}
								progressDOM.find('.current').html(current);
								progressDOM.find('.total').html(total);
							}
								
						}
					},
					navigation: {
						nextEl: '.mynext-button',
						prevEl: '.myprev-button',
					},
					breakpoints: {
						0: {
							slidesPerView: 1,
							spaceBetween: 20,
						},
						768: {
							slidesPerView: 1,
							spaceBetween: 20,
						},
						1200: {
							slidesPerView: 2,
							spaceBetween: 20,
						},
						1600: {
							slidesPerView: 3,
							spaceBetween: 70
						}
					}
				});
			});
			Industify.imgToSVG();
		},
		
		counter: function(){
			var element = $('.fn_cs_counter');
			element.each(function() {
				var el 	= $(this);
				el.waypoint({
					handler: function(){
						if(!el.hasClass('stop')){
							el.addClass('stop').countTo({
								refreshInterval: 50,
								formatter: function (value, options) {
									return value.toFixed(options.decimals).replace(/\B(?=(?:\d{3})+(?!\d))/g, ',');
								},	
							});
						}
					},
					offset:'90%'	
				});
			});
		},
		
		spacer: function(){
			$('[data-margin-bottom]').each(function(){
				var e = $(this);
				e.css({marginBottom:e.data('margin-bottom') + 'px'});
			});
			$('[data-margin-top]').each(function(){
				var e = $(this);
				e.css({marginTop:e.data('margin-top') + 'px'});
			});
			$('[data-padding-bottom]').each(function(){
				var e = $(this);
				e.css({paddingBottom:e.data('padding-bottom') + 'px'});
			});
			$('[data-padding-top]').each(function(){
				var e = $(this);
				e.css({paddingTop:e.data('padding-top') + 'px'});
			});
		},
		
		popupYoutube: function(){
			$('.popup-youtube').each(function() { // the containers for all your galleries
				$(this).magnificPopup({
					disableOn: 700,
					type: 'iframe',
					mainClass: 'mfp-fade',
					removalDelay: 160,
					preloader: false,
					fixedContentPos: false
				});
			});	
		},
		
		
		kenburnsy: function(){
			var kenburns 		= $('.fn_cs_kenburnsy');
			kenburns.each(function(){
				var element 	= $(this);
				var duration 	= element.data('interval');
				element.kenburnsy({
					fullscreen: true,
					duration: duration,
				});
			});
		},
		
		isotope: function(){
			var masonry = $('.masonry');
			if($().isotope){
				masonry.each(function(){
					$(this).isotope({
					  itemSelector: '.masonry_in',
					  masonry: {

					  }
					});
				});
			}	
		},
		
		lightGallery: function(){
			if($().lightGallery){
				// FIRST WE SHOULD DESTROY LIGHTBOX FOR NEW SET OF IMAGES

				var gallery = $('.fn_cs_lightgallery');

				gallery.each(function(){
					var element = $(this);
					element.lightGallery(); // binding
					if(element.length){element.data('lightGallery').destroy(true); }// destroying
					$(this).lightGallery({
						selector: ".lightbox",
						thumbnail: 1,
						loadYoutubeThumbnail: !1,
						loadVimeoThumbnail: !1,
						showThumbByDefault: !1,
						mode: "lg-fade",
						download:!1,
						getCaptionFromTitleOrAlt:!1,
					});
				});
			}	
		},
		
		supportBlockBgCalc: function(){
			var sBlock 		= $('.fn_cs_support_block .support_block');
			sBlock.each(function(){
				var el 		= $(this);
				var height 	= el.outerHeight() - 30;
				el.find('.img_wrap span').css({borderTopWidth: height + 'px'});
			});
		},
		
		triangleCalc: function(){
			var tollFree 	= $('.industify_fn_header .toll_free');
			if(tollFree.length){
				var shape2	= tollFree.find('span.shape2');
				var shape3	= tollFree.find('span.shape3');
				var tfoh	= tollFree.outerHeight();
				shape2.css({borderTopWidth: (tfoh - 18) + 'px'});
				shape3.css({borderTopWidth: tfoh + 'px'});
			}
			var tollFreeM 	= $('.industify_fn_mobilemenu_wrap .m_toll_free');
			if(tollFreeM.length){
				var shape2M	= tollFreeM.find('span.shape2');
				var shape3M	= tollFreeM.find('span.shape3');
				var tfohM	= tollFreeM.outerHeight();
				shape2M.css({borderTopWidth: (tfohM - 18) + 'px'});
				shape3M.css({borderTopWidth: tfohM + 'px'});
			}
		},
		
		mobileSubmenuOpener: function(){
			$('.vert_menu_list a').on('click', function(){
				var element 			= $(this);
				var parentItem			= element.parent('li');
				var parentItems			= element.parents('li');
				var parentUls			= parentItem.parents('ul.sub-menu');
				var subMenu				= element.next();
				var parent				= element.closest('.vert_menu_list');
				var allSubMenusParents 	= parent.find('li');

				allSubMenusParents.removeClass('opened');

				if(subMenu.length){

					if(!(parentItem.hasClass('active'))){
						if(!(parentItems.hasClass('opened'))){parentItems.addClass('opened');}

						allSubMenusParents.each(function(){
							var el = $(this);
							if(!el.hasClass('opened')){el.find('ul.sub-menu').slideUp();}
						});

						allSubMenusParents.removeClass('active');
						parentUls.parent('li').addClass('active');
						parentItem.addClass('active');
						subMenu.slideDown();


					}else{
						parentItem.removeClass('active');
						subMenu.slideUp();
					}
					return false;
				}
			});
		},
		
		mobileMenuOpener: function(){
			var hamburger		= $('.industify_fn_mobilemenu_wrap .hamburger');
			hamburger.on('click',function(){
				var element 	= $(this);
				var menupart	= $('.industify_fn_mobilemenu_wrap .mobilemenu');
				if(element.hasClass('is-active')){
					element.removeClass('is-active');
					menupart.removeClass('opened');
					menupart.slideUp(500);
				}else{
					element.addClass('is-active');
					menupart.addClass('opened');
					menupart.slideDown(500);
				}return false;
			});	
		},
		
		languageCalc: function(){
			var movingLang 	= $('.industify_fn_moving_lang');
			if(movingLang.length){
				var lang 		= $('.lang_switcher');
				var langTO		= lang.offset().top;
				var langLO		= lang.offset().left;
				movingLang.css({position: 'absolute',left: langLO + 'px',top: langTO + 30 + 'px'});
			}
		},
		
		languageOpener: function(){
			var lang 		= $('.lang_switcher');
			if(lang.length){
				var click 		= lang.find('span.click');
				var box 		= lang.find('ul');
				var langTO		= lang.offset().top;
				var langLO		= lang.offset().left;
				var wrapper		= $('.industify_fn_wrapper_all');
				wrapper.append('<div class="industify_fn_moving_lang"><ul>'+box.html() + '</ul></div>');
				var movingLang 	= $('.industify_fn_moving_lang');
				var box2		= movingLang.find('ul');
				movingLang.css({position: 'absolute',left: langLO + 'px',top: langTO + 30 + 'px'});

				if(lang.length){
					click.on('click',function(){
						if(lang.hasClass('opened')){
							movingLang.removeClass('opened');
							lang.removeClass('opened');
						}else{
							lang.addClass('opened');
							movingLang.addClass('opened');
						}
					});
					$(window).on('click',function() {
						lang.removeClass('opened');
						movingLang.removeClass('opened');
					});
					box2.on('click',function(event){
						event.stopPropagation();
					});
					lang.on('click',function(event){
						event.stopPropagation();
					});
				}
			}

		},

		
		totop: function(){
			var totop = $('.industify_fn_totop');
			if(totop.length){
				totop.on('click', function(e) {
					e.preventDefault();
					var speed 	= totop.offset().top/5;
					var min		= 500;
					var max		= 1500;
					speed = (speed > max) ? max: speed;
					speed = (speed < min) ? min: speed;
					$("html, body").animate({ scrollTop: 0 }, speed);
					return false;
				});
			}
		},
		
		serviceQueryCarousel: function(){
			var owl			 	= $('.fn_cs_service_query .owl-carousel');
			owl.each(function(){
				var el 			= $(this);
				var parent		= el.closest('.fn_cs_service_query');
				var count 		= parseInt(parent.data('column-count'));
				if(!$.isNumeric(count)){count = 4;}
				var responsive1400,responsive1200,responsive480;
				switch(count){
					case 5: responsive1400 = 5; responsive1200 = 4; responsive480 = 2; break;
					case 4: responsive1400 = 4; responsive1200 = 3; responsive480 = 2; break;
					case 3: responsive1400 = 3; responsive1200 = 3; responsive480 = 2; break;
					case 2: responsive1400 = 2; responsive1200 = 2; responsive480 = 2; break;
					case 1: responsive1400 = 1; responsive1200 = 1; responsive480 = 1; break;
				}
				el.owlCarousel({
					loop: true,
					margin: 0,
					nav: false,
				 	items: 4,
					dots: false,
					smartSpeed: 1000,
					responsive : {
						0 : {items : 1},
						480 : {items : responsive480},
						1200 : {items : responsive1200},
						1400 : {items : responsive1400}
					}
				});
				var prev = parent.find('.owl_control .fn_prev');
				var next = parent.find('.owl_control .fn_next');
				prev.on('click',function(){
					el.trigger('prev.owl');
					return false;
				});
				next.on('click',function(){
					el.trigger('next.owl');
					return false;
				});
				Industify.imgToSVG();
			});
			Industify.imgToSVG();
			Industify.BgImg();
		},
		
		parallax: function(){
			$('#scene').parallax();
		},
		
		alphaSlider: function(){
			Industify.BgImg();
			$('.industify_slider_alpha').each(function(){
				var images 			= $(this);
				var autoplaySwitch 	= images.data('autoplay-switch');
				var effect		 	= images.data('effect');
				var autoplayTime;
				if(autoplaySwitch === 'enabled'){
					autoplayTime 	= images.data('autoplay-time');
				}else{
					autoplayTime 	= 80000;
				}
				var imagesSlider 	= new Swiper(images, {
					centeredSlides: false,
					slideToClickedSlide: false,
					slidesPerView: 1,
					spaceBetween: 0,
					preloadImages: false,
					lazyLoading: false,
					autoplay: {
						delay: autoplayTime,
						disableOnInteraction: false
					},
					initialSlide:0,
					navigation: {
						nextEl: images.find('.fn_next'),
						prevEl: images.find('.fn_prev'),
					  },
					effect: effect,
					coverflowEffect: {
						rotate: 30,
						slideShadows: false,
					},
					flipEffect: {
						rotate: 30,
						slideShadows: false,
					},
					cubeEffect: {
						slideShadows: false,
					},
					loop: true,
					pagination: {
						el: images.find('.swiper-pagination'),
						type: 'progressbar',
					},
					speed: 1000
				});
			});	
		},
		
		imgToSVG: function(){
			$('img.fn__svg').each(function(){
				var img 		= $(this);
				var imgClass	= img.attr('class');
				var imgURL		= img.attr('src');

				$.get(imgURL, function(data) {
					var svg 	= $(data).find('svg');
					if(typeof imgClass !== 'undefined') {
						svg 	= svg.attr('class', imgClass+' replaced-svg');
					}
					img.replaceWith(svg);

				}, 'xml');

			});	
		},

	  	BgImg: function(){
			var div = $('*[data-bg-img]');
			div.each(function(){
				var element = $(this);
				var attrBg	= element.attr('data-bg-img');
				if(typeof(attrBg) !== 'undefined'){
					element.css({backgroundImage:'url('+attrBg+')'});
				}
			});
			var div2 = $('*[data-fn-bg-img]');
			div2.each(function(){
				var element = $(this);
				var attrBg	= element.attr('data-fn-bg-img');
				if(typeof(attrBg) !== 'undefined'){
					element.css({backgroundImage:'url('+attrBg+')'});
				}
			});
		},
		
		contactForm: function(){
			$('#send_message').on('click', function(){
				var form		= $('.contact_form');
				var name 		= $("#name").val();
				var email 		= $("#email").val();
				var message 	= $("#message").val();
				var spanSuccess	= form.find(".success");
				var success     = spanSuccess.data('success');
				var emailto     = form.data('email');

				spanSuccess.empty();
				if(name === ''|| email === ''|| message === '' || emailto === ''){
					$('.empty_notice').slideDown(500).delay(2000).slideUp(500);
				}
				else{
					$.post(
						"modal/contact.php",
						{
							ajax_name: 		name,
							ajax_email: 	email,
							ajax_emailto: 	emailto,
							ajax_message: 	message
						}, function(data) {
							spanSuccess.append(data);
							if(spanSuccess.find(".contact_error").length){
								spanSuccess.slideDown(500).delay(2000).slideUp(500);		
							}else{
								spanSuccess.append("<span class='contact_success'>" + success + "</span>");
								spanSuccess.slideDown(500).delay(4000).slideUp(500);
							}
							if(data === ''){ form[0].reset();}
						}
					);
				}
				return false; 
			});
		},
    
  	};
  	
	
	// READY Functions
	$(document).ready(function(){
		Industify.getIncludedHTML();
	});
	
	// RESIZE Functions
	$(window).on('resize',function(){
		Industify.isotope();
		Industify.triangleCalc();
		Industify.languageCalc();
		Industify.supportBlockBgCalc();
		Industify.reCalcProjectElegant();
		Industify.estimateWidgetCalc();
		Industify.blogShapeCalc();
	});
	
	
	
	// LOAD Functions
	$(window).on('load',function(){
		
		$('body').addClass('preloader_loaded');
		
		Industify.isotope();
		
		setTimeout(function(){
			
			if($('.industify_fn_portfolio_list').length){
				$('.industify_fn_portfolio_list').isotope({});
			}
			Industify.isotope();
		},600);
	});
  
})(jQuery);