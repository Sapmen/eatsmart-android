from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

Window.clearcolor = (0.04, 0.04, 0.06, 1)

class EatSmartApp(App):
    def build(self):
        self.total_kcal = 0
        
        main = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        title = Label(text='🍎 Eat Smart', font_size=36, color=(0,1,0.62,1), size_hint_y=0.1)
        main.add_widget(title)
        
        self.search = TextInput(hint_text='🔍 Введи любое блюдо...', size_hint_y=0.08, 
                                background_color=(0.1,0.1,0.18,1), foreground_color=(1,1,1,1))
        self.search.bind(text=self.on_search)
        main.add_widget(self.search)
        
        self.result = Label(text='', size_hint_y=0.07, color=(0,1,0.62,1))
        main.add_widget(self.result)
        
        weight_box = BoxLayout(size_hint_y=0.08, spacing=10)
        weight_box.add_widget(Label(text='Вес (г):', color=(1,1,1,1), size_hint_x=0.3))
        self.weight_input = TextInput(text='100', multiline=False, background_color=(0.1,0.1,0.18,1), foreground_color=(1,1,1,1))
        weight_box.add_widget(self.weight_input)
        main.add_widget(weight_box)
        
        add_btn = Button(text='➕ ДОБАВИТЬ', size_hint_y=0.08, background_color=(0,1,0.62,1), color=(0,0,0,1))
        add_btn.bind(on_press=self.add_food)
        main.add_widget(add_btn)
        
        water_label = Label(text='💧 ВОДА', size_hint_y=0.05, color=(0,0.72,1,1))
        main.add_widget(water_label)
        
        water_grid = GridLayout(cols=4, size_hint_y=0.12, spacing=5)
        for vol in [200, 250, 300, 500, 750, 1000]:
            btn = Button(text=str(vol), background_color=(0,0.72,1,1), color=(0,0,0,1))
            btn.bind(on_press=lambda x, v=vol: self.add_water(v))
            water_grid.add_widget(btn)
        main.add_widget(water_grid)
        
        self.stats = Label(text='🔥 К: 0 / 2200\n🥩 Б: 0 / 120\n🥑 Ж: 0 / 80\n🍚 У: 0 / 300\n💧 0 / 2500', 
                           font_size=12, color=(0.9,0.9,0.9,1), size_hint_y=0.25, halign='left', valign='top')
        self.stats.bind(size=self.stats.setter('text_size'))
        main.add_widget(self.stats)
        
        btn_box = BoxLayout(size_hint_y=0.08, spacing=5)
        save_btn = Button(text='💾 СОХР', background_color=(0,1,0.62,1), color=(0,0,0,1))
        save_btn.bind(on_press=self.save_data)
        load_btn = Button(text='📂 ЗАГР', background_color=(0,0.72,1,1), color=(0,0,0,1))
        load_btn.bind(on_press=self.load_data)
        reset_btn = Button(text='🔄 СБР', background_color=(1,0.28,0.34,1), color=(1,1,1,1))
        reset_btn.bind(on_press=self.reset_data)
        btn_box.add_widget(save_btn)
        btn_box.add_widget(load_btn)
        btn_box.add_widget(reset_btn)
        main.add_widget(btn_box)
        
        return main
    
    def on_search(self, instance, value):
        if value:
            self.result.text = f'✨ Найдено: {value.capitalize()}'
        else:
            self.result.text = ''
    
    def add_food(self, instance):
        try:
            weight = float(self.weight_input.text)
            if self.result.text and self.result.text != '':
                kcal = 100 * weight / 100
                self.total_kcal += kcal
                self.update_stats()
                self.result.text = f'✅ Добавлено!'
        except:
            self.result.text = '❌ Ошибка! Введите число'
    
    def add_water(self, ml):
        pass
    
    def update_stats(self):
        self.stats.text = f'🔥 К: {self.total_kcal:.0f} / 2200\n🥩 Б: 0 / 120\n🥑 Ж: 0 / 80\n🍚 У: 0 / 300\n💧 0 / 2500'
    
    def save_data(self, instance):
        pass
    
    def load_data(self, instance):
        pass
    
    def reset_data(self, instance):
        self.total_kcal = 0
        self.update_stats()
        self.result.text = '🔄 Сброшено'

if __name__ == '__main__':
    EatSmartApp().run()
