def make_shirt(size='large', text='I love python'):
    """Show the shirt size and text"""
    print(f"You ordered t-shirt which size is {size}.")
    print(f"You wanted following text on your shirt: {text}")

make_shirt('medium', 'Hello World!')
make_shirt()
make_shirt(size='medium')