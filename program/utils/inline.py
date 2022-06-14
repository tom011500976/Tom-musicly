""" inline section button """


from pyrogram.types import (
  InlineKeyboardButton,
  InlineKeyboardMarkup,
)


def stream_markup(user_id):
  buttons = [
    [
      InlineKeyboardButton(text="-› تَحَكَمَ", callback_data=f'stream_menu_panel | {user_id}'),
      InlineKeyboardButton(text="-› اެغِݪاެقِ", callback_data=f'set_close'),
    ],
  ]
  return buttons


def menu_markup(user_id):
  buttons = [
    [
      InlineKeyboardButton(text="⏹", callback_data=f'set_stop | {user_id}'),
      InlineKeyboardButton(text="⏸", callback_data=f'set_pause | {user_id}'),
      InlineKeyboardButton(text="▶️", callback_data=f'set_resume | {user_id}'),
      InlineKeyboardButton(text="⏭", callback_data=f'set_skip | {user_id}'),
    ],
    [
      InlineKeyboardButton(text="🔇", callback_data=f'set_mute | {user_id}'),
      InlineKeyboardButton(text="🔊", callback_data=f'set_unmute | {user_id}'),
    ],
    [
      InlineKeyboardButton(text="-› ࢪجَۅٛعَ", callback_data='stream_home_panel'),
    ]
  ]
  return buttons


close_mark = InlineKeyboardMarkup(
  [
    [
      InlineKeyboardButton(
        "-› اެغِݪاެقِ", callback_data="set_close"
      )
    ]
  ]
)


back_mark = InlineKeyboardMarkup(
  [
    [
      InlineKeyboardButton(
        "-› ࢪجَۅٛعَ", callback_data="stream_menu_panel"
      )
    ]
  ]
)
