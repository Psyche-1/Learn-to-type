// For learn
// http://ruseller.com
// https://api.jquery.com/
// http://javascript.ru/tutorial/foundation
// https://jquery.com/download/
/*
Дисклеймер: Идея не моя, но реализация полностью моя.
*/
//<link href="style.css" rel="stylesheet" type="text/css"/>

languages = ['eng', 'рус', 'укр', ]


// Choose using symbols and texts
user_enter = true
number_of_word = 10

//user_enter = false  // uncomment for test
if ( !user_enter ) {
		use = 'укр'
		word_n = 0
	}

//alert('ИНСТРУКЦИЯ')

while ( user_enter ) {
	use = prompt('Enter language: eng, рус, укр', 'укр')
	
	for( var i=0; i<languages.length; i++ ) {
		if ( use == languages[i] ) {
			user_enter = false
		}
	}
	if ( user_enter ) {
		alert('Wrong language!')
	}
	
	word_n = Number(prompt(number_of_word_smss[use], 0))
	//number_of_word = Number(prompt('Enter number of words to be displayed: ', '10'))
}

use_symbols = symbols[use]
use_text = text[use]
use_end = ends[use]
backspace = backspaces[use]
use_number_of_word_show = number_of_word_show[use]


// Rewright use text + end
text = []
for( var i=0; i<use_text.length; i++ ) {
	text.push(use_text[i])
}

for( var i=0; i<number_of_word; i++ ) {
	text.push(use_end)
}


// Script
jQuery('document').ready(function() {
	//word_n = 0
	sym_n = 0
	
	// First emergence in result and check
	jQuery('#result').html( text.slice(word_n, word_n + number_of_word) )
	jQuery('.image1').attr("src","Typing_files/js/Правая рука.png")
	jQuery('#check').html( "'" + text[word_n][sym_n] + "'	" + use_symbols[text[word_n][sym_n]] )
	
	jQuery('#num').html( use_number_of_word_show + word_n )
	
	jQuery('#value').on('keyup', function() {
		
		type = jQuery('#value').val()
		
		if ( type == text[word_n] ) {  // Next word
			word_n++
			sym_n = 0
			jQuery('#value').val( '' )
		} else {
			jQuery('#err').html( '' )
			if ( type[sym_n] == text[word_n][sym_n] ) {  // Next symbol
				sym_n++
			} else if ( type.length > sym_n ) {
				jQuery('#err').html( backspace )
			}
		}
		
		// Next emergence in result and check
		jQuery('#result').html( text.slice(word_n, word_n + number_of_word) )
		jQuery('.image1').attr("src","Typing_files/js/Правая рука.png")
		jQuery('#check').html( "'" + text[word_n][sym_n] + "'	" + use_symbols[text[word_n][sym_n]] )
		jQuery('#num').html( use_number_of_word_show + word_n )
		
		if ( text[word_n] == use_end ) {  // End
			jQuery('#result').html( text[word_n] )
			jQuery('#err').html( 'Completed!' )
			jQuery('#check').html( 'Congratulation!' )
			jQuery('#num').html( use_number_of_word_show + word_n )
		}
	})
})