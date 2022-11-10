# -*- coding: utf-8 -*-
#


from random import shuffle

from telegram import (ParseMode, ReplyKeyboardMarkup, ReplyKeyboardRemove,
                      KeyboardButton)
from telegram.ext import (Updater, CommandHandler, RegexHandler,
                          ConversationHandler)

from tic_tac_toe import TicTacToe

import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - \
                    %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)

INIT_GAME, GAME_LOOP, GAME_OVER = range(3)

# Create TicTacToe class instance
tic_tac_toe = TicTacToe()

# Reply keyboard for user's move(from 1 to 9)
reply_num_keyboard = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3']
]

# Reply keyboard for user's answer on "Yes/No" questions
# (In particular, Do you want to play again? (yes or no) )
reply_yes_no_keyboard = [[KeyboardButton('yes'), KeyboardButton('no')]]


def play_again_msg(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text='Do you want to play again? (yes or no)',
        reply_markup=ReplyKeyboardMarkup(
            reply_yes_no_keyboard,
            resize_keyboard=True
        )
    )


def user_next_move_prompt_msg(bot, update, board):
    # Drawn the game's board
    update.message.reply_text(tic_tac_toe.get_drawn_board(board))
    logger.info('board = %s', board)

    # Send message for the human's next move
    bot.send_message(
        chat_id=update.message.chat_id,
        text='What is the next move(1-9)',
        reply_markup=ReplyKeyboardMarkup(
            reply_num_keyboard
        )
    )


def bot_move(bot, update, board, bot_game_letter):
    logger.info('Make next bot\'s move')

    move = tic_tac_toe.get_bot_move(
        board,
        bot_game_letter
    )

    tic_tac_toe.make_move(
        board,
        bot_game_letter,
        move
    )

    update.message.reply_text(
        'Bot mark {} on {} cell'.
        format(bot_game_letter, str(move))
    )


def analyze_bot_move(bot, update, board, bot_game_letter):
    logger.info('Analysis of the game situation after the bot\'s move')

    if tic_tac_toe.is_winner(board, bot_game_letter):
        update.message.reply_text(
            tic_tac_toe.get_drawn_board(board)
        )
        update.message.reply_text(
            'The Bot has beaten you! You lose.'
        )

        # Send message as question for the play again
        play_again_msg(bot, update)

        return GAME_OVER
    else:
        if tic_tac_toe.is_board_full(board):
            update.message.reply_text(
                tic_tac_toe.get_drawn_board(board)
            )
            update.message.reply_text('The game is tie!')

            # Send message as question for the play again
            play_again_msg(bot, update)

            return GAME_OVER
        else:
            # Set next turn for the user
            logger.info('Set the user\'s turn after bot\'s move \
            (Current state: GAME_LOOP)')

            current_turn = tic_tac_toe.get_turn()
            logger.info('current turn = %s', current_turn)

            tic_tac_toe.set_next_turn(current_turn)
            logger.info('next turn = %s', tic_tac_toe.get_turn())

            user_next_move_prompt_msg(bot, update, board)

            return GAME_LOOP


def start(bot, update):

    logger.info('Start game with /start command')

    # Check GAME_OVER state
    user = update.message.from_user
    user_choice = update.message.text

    if user_choice.lower().startswith('n'):

        logger.info(
            "User %s answer \'%s\' on play again question.",
            user.first_name,
            user_choice
        )

        update.message.reply_text('Bye! Game over.',
                                  reply_markup=ReplyKeyboardRemove())

        # The game is ended.
        return ConversationHandler.END

    # Start new game or play game again

    # Create and shuffle game_letters list
    game_letters = ['X', 'O']
    shuffle(game_letters)

    # Create reply_keyboard list from game_letters list
    reply_keyboard = list()
    for letter in game_letters:
        reply_keyboard.append(letter)

    # Get user data from user's message
    user = update.message.from_user

    # Send welcome message
    bot.send_message(
        chat_id=update.message.chat_id,
        text='Hi {}! \n\n\
        Welcome to Tic Tac Toe! \n\n\
        My name is {}. I will game with you.\n'
             'Send /cancel to stop game.\n\n'
             'Send /rules to get game rules.'.format(user.first_name, bot.username)
    )

    # Send message which to let the user select game letter.
    bot.send_message(
        chat_id=update.message.chat_id,
        text='Do you want to be X or O ?',
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard
        )
    )

    # Transition to INIT_GAME state
    return INIT_GAME


def init_game(bot, update):

    logger.info('Current state: INIT_GAME')

    user = update.message.from_user
    user_game_letter = update.message.text
    logger.info(
        "Player %s choice %s ",
        user.first_name,
        user_game_letter
    )

    # Init the board (size 3 x 3 cells) for playing Tic-Tac-Toe
    # As a list of 10 elements(The board[0] element will not use).
    tic_tac_toe.init_board()

    board = tic_tac_toe.get_board()
    logger.info('board = %s', board)

    # Depending on the chosen a user's letter ('X' or 'O'),
    # set the game letters for both opponents
    tic_tac_toe.set_game_letters(user_game_letter)

    user_game_letter = tic_tac_toe.get_user_game_letter()
    bot_game_letter = tic_tac_toe.get_bot_game_letter()

    logger.info(
        "user_game_letter = %s, bot_game_letter = %s",
        user_game_letter,
        bot_game_letter
    )

    update.message.reply_text(
        '{}, you have chosen to play {}\n\
        Your opponent {} will use the {}'.
        format(
            user.first_name,
            user_game_letter,
            bot.username,
            bot_game_letter
        )
    )

    # Randomly choose which player goes first.
    tic_tac_toe.set_turn()

    current_turn = tic_tac_toe.get_turn()

    logger.info("%s was randomly selected for the first move",
                current_turn)

    if current_turn == 'user':
        # User's first turn
        logger.info('User\'s first turn (Current state: INIT_GAME)')

        update.message.reply_text(
            '{}, you are given the first move by {}'.
            format(user.first_name, user_game_letter)
        )

        # Send message for the user's next move
        user_next_move_prompt_msg(bot, update, board)

        return GAME_LOOP
    else:
        # Bot's first turn
        logger.info('Bot\'s first turn (Current state: INIT_GAME)')

        # Send message for the Bot's first move
        update.message.reply_text(
            'The right of the first move is granted to the {}'.
            format(bot.username)
        )

        # Execute the current move of the bot
        bot_move(bot, update, board, bot_game_letter)

        # Analyze the current move of the bot
        next_game_state = analyze_bot_move(
            bot, update, board, bot_game_letter)

        return next_game_state


def game_loop(bot, update):

    logger.info('Current state: GAME_LOOP')

    board = tic_tac_toe.get_board()
    logger.info('board = %s', board)

    current_turn = tic_tac_toe.get_turn()
    logger.info('current turn = %s', current_turn)

    if current_turn == 'user':
        # User's turn
        logger.info('User\'s turn (Current state: GAME_LOOP)')

        user_game_letter = tic_tac_toe.get_user_game_letter()
        logger.info('user game letter = %s', user_game_letter)

        check_move = int(update.message.text)
        logger.info('check_move (for user) = %d', check_move)

        update.message.reply_text(
            'User mark {} on {} cell'.
            format(user_game_letter, str(check_move))
        )

        if not tic_tac_toe.is_space_free(board, check_move):
            update.message.reply_text(
                'Cell {} is busy. Please, select another cell for the move'.
                format(str(check_move))
            )

            # Send message for the user's next move
            user_next_move_prompt_msg(bot, update, board)

            return GAME_LOOP

        else:
            tic_tac_toe.make_move(board, user_game_letter, check_move)

            if tic_tac_toe.is_winner(board, user_game_letter):
                update.message.reply_text(tic_tac_toe.get_drawn_board(board))
                update.message.reply_text('Hooray! You have won the game!')

                # Send message as question for the play again
                play_again_msg(bot, update)

                return GAME_OVER

            else:
                if tic_tac_toe.is_board_full(board):
                    update.message.reply_text(
                        tic_tac_toe.get_drawn_board(board)
                    )
                    update.message.reply_text('The game is tie!')

                    # Send message as question for the play again
                    play_again_msg(bot, update)

                    return GAME_OVER

                else:
                    # Set next turn for the Bot
                    logger.info('Set the Bot\'s turn after User\'s move \
                    (Current state: GAME_LOOP)')

                    logger.info('current turn = %s', current_turn)

                    tic_tac_toe.set_next_turn(current_turn)
                    logger.info('next turn = %s', tic_tac_toe.get_turn())

                    bot_game_letter = tic_tac_toe.get_bot_game_letter()
                    logger.info('bot game letter = %s', bot_game_letter)

                    # Execute the current move of the bot
                    bot_move(bot, update, board, bot_game_letter)

                    # Analyze the current move of the bot
                    next_game_state = analyze_bot_move(
                        bot, update, board, bot_game_letter)

                    return next_game_state

    else:
        # Bot's turn
        logger.info('Bot\'s turn (Current state: GAME_LOOP)')

        bot_game_letter = tic_tac_toe.get_bot_game_letter()

        bot_move(bot, update, board, bot_game_letter)

        # Analyze the current move of the bot
        next_game_state = analyze_bot_move(
            bot, update, board, bot_game_letter)

        return next_game_state


def game_rules(bot, update):

    user = update.message.from_user
    logger.info("User %s send /rules command.", user.first_name)

    # Send text message with short rules of the Tic-Tac-Toe game
    bot.send_message(
        chat_id=update.message.chat_id,
        text='*Tic-Tac-Toe game rules.* \n\n'
             'Tic-Tac-Toe is normally played with two people.\n'
             'However, in this game your opponent will be a Bot ({}).\n'
             'One player is X and the other player is O.\n'
             'Players take turns placing their X or O.\n'
             'If a player gets three of their marks on the board in a row, \
             column, or diagonal, they win.\n'
             'Then the board fills up with neither player winning, \
             the game ends in a draw.\n\n'
             '*How to make move*\n\n'
             'The player makes their move by entering the number of the space \
             they want to take.\n'
             'To help us remember which index in the list is for which space, \
             we will number the board like a keyboard\'s number pad \
             (please, see image below).\n\n'
             '*Use custom keyboards*\n\n'
             'For ease of interaction with the bot during the game, \
             it is recommended to use the following special custom keyboards:\n'
             '- to select a game letter (X or O)\n'
             '- to perform the next move on the board (from 1 to 9)\n'
             '- to answer the question of the completion or the beginning \
             of a new game (yes or no)'.
        format(bot.username), parse_mode=ParseMode.MARKDOWN
    )

    # Send image with number the board like a keyboard's number pad
    bot.send_photo(
        chat_id=update.message.chat_id,
        photo=open('images/board_numbering_359x216.png', 'rb')
    )

    return INIT_GAME


def cancel(bot, update):

    user = update.message.from_user
    logger.info("User %s canceled the game.", user.first_name)
    update.message.reply_text('Bye! Game canceled by user.',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END


def error(bot, update, error):

    logger.warning('Update "%s" caused error "%s"', update, error)


def main():

    # Create the EventHandler and pass it your bot's token.
    updater = Updater('token')

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add conversation handler with the following states:
    # INIT_GAME, GAME_LOOP, and GAME_OVER
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            INIT_GAME: [RegexHandler('^(X|O)$', init_game),
                        CommandHandler('rules', game_rules)],


            GAME_LOOP: [RegexHandler('^(1|2|3|4|5|6|7|8|9)$',
                                     game_loop)],

            GAME_OVER: [RegexHandler('^(yes|no)$', start)]

        },

        fallbacks=[CommandHandler('cancel', cancel)]
    )

    # Register conversation handler in the dispatcher
    dp.add_handler(conv_handler)

    # Log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()