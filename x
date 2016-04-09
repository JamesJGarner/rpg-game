[1mdiff --git a/game/templates/characters/character_detail.html b/game/templates/characters/character_detail.html[m
[1mindex f675525..01db7ef 100644[m
[1m--- a/game/templates/characters/character_detail.html[m
[1m+++ b/game/templates/characters/character_detail.html[m
[36m@@ -24,82 +24,78 @@[m
   <li class="tabs-title"><a href="#panel2">Spells</a></li>[m
   <li class="tabs-title"><a href="#panel3">Statistics</a></li>[m
 </ul>[m
[32m+[m
 <div class="tabs-content" data-tabs-content="example-tabs">[m
   <div class="tabs-panel is-active" id="panel1">[m
     <div class="large-8 columns cd-no-padding">[m
[31m-    {% if character.itemacquired_set.all %}[m
[31m-    <ul class="cd-inventory-bag">[m
[31m-        {% for item in character.itemacquired_set.all  %}[m
[31m-        <li id="inv-{{ item.id }}"  {% if item.equipped_to %}class="cd-item-hide"{% endif %}>[m
[31m-          <img src="{{ item.item.icon.url }}">[m
[31m-        </li>[m
[31m-        [m
[31m-        <div id="inv-{{ item.id }}-dropdown" class="cd-spell-hide">[m
[31m-          <ul class="cd-spell-detail">[m
[31m-            <li><img src="{{ item.item.icon.url }}"></li>[m
[31m-            <li><h4>{{ item.item.name  }}</h4></li>[m
[31m-            <li>Damage: {{ item.item.damage }}</li>[m
[31m-            <li>Healing: {{ item.item.healing }}</li>[m
[31m-            <li>Armor: {{ item.item.armor }}</li>[m
[31m-          </ul>[m
[31m-        </div>[m
[31m-        {% endfor %}[m
[31m-        [m
[31m-    </ul>[m
[31m-    {% endif %}[m
[31m-  </div>[m
[31m-  <div class="large-4 columns cd-no-padding">[m
[31m-  <div class="cd-spell-sidebar" id="inv-sidebar">[m
[31m-  </div>[m
[31m-  </div>[m
[32m+[m[32m      {% if character.itemacquired_set.all %}[m
[32m+[m[32m      <ul class="cd-inventory-bag">[m
[32m+[m[32m          {% for item in character.itemacquired_set.all  %}[m
[32m+[m[32m          <li id="inv-{{ item.id }}"  {% if item.equipped_to %}class="cd-item-hide"{% endif %}>[m
[32m+[m[32m            <img src="{{ item.item.icon.url }}">[m
[32m+[m[32m          </li>[m[41m    [m
[32m+[m[32m          <div id="inv-{{ item.id }}-dropdown" class="cd-spell-hide">[m
[32m+[m[32m            <ul class="cd-spell-detail">[m
[32m+[m[32m              <li><img src="{{ item.item.icon.url }}"></li>[m
[32m+[m[32m              <li><h4>{{ item.item.name  }}</h4></li>[m
[32m+[m[32m              <li>Damage: {{ item.item.damage }}</li>[m
[32m+[m[32m              <li>Healing: {{ item.item.healing }}</li>[m
[32m+[m[32m              <li>Armor: {{ item.item.armor }}</li>[m
[32m+[m[32m            </ul>[m
[32m+[m[32m          </div>[m
[32m+[m[32m          {% endfor %}[m
[32m+[m[32m      </ul>[m
[32m+[m[32m      {% endif %}[m
[32m+[m[32m    </div>[m
[32m+[m[32m    <div class="large-4 columns cd-no-padding">[m
[32m+[m[32m      <div class="cd-spell-sidebar" id="inv-sidebar"></div>[m
[32m+[m[32m    </div>[m
   </div>[m
   <div class="tabs-panel" id="panel2">[m
[31m-  <div class="large-8 columns cd-no-padding">[m
[31m-  <ul class="cd-spells">[m
[31m-  {% for item in spells %}[m
[31m-    <li id="spell-{{ item.id }}"><img src="{{ item.spell.image.url }}"></li>[m
[31m-    <div id="spell-{{ item.id }}-dropdown" class="cd-spell-hide">[m
[31m-      <ul class="cd-spell-detail">[m
[31m-        <li><img src="{{ item.spell.image.url }}"></li>[m
[31m-        <li><h4>{{ item.spell.name }}</h4></li>[m
[31m-        <li>Spell Damage: {{ item.spell.damage }}</li>[m
[31m-        <li>Level Required: {{ item.spell.level_required }}</li>[m
[31m-        <li>Turn Cooldown: {{ item.spell.turn_cooldown }}</li>[m
[32m+[m[32m    <div class="large-8 columns cd-no-padding">[m
[32m+[m[32m      <ul class="cd-spells">[m
[32m+[m[32m        {% for item in spells %}[m
[32m+[m[32m          <li id="spell-{{ item.id }}"><img src="{{ item.spell.image.url }}"></li>[m
[32m+[m[32m          <div id="spell-{{ item.id }}-dropdown" class="cd-spell-hide">[m
[32m+[m[32m            <ul class="cd-spell-detail">[m
[32m+[m[32m              <li><img src="{{ item.spell.image.url }}"></li>[m
[32m+[m[32m              <li><h4>{{ item.spell.name }}</h4></li>[m
[32m+[m[32m              <li>Spell Damage: {{ item.spell.damage }}</li>[m
[32m+[m[32m              <li>Level Required: {{ item.spell.level_required }}</li>[m
[32m+[m[32m              <li>Turn Cooldown: {{ item.spell.turn_cooldown }}</li>[m
[32m+[m[32m            </ul>[m
[32m+[m[32m          </div>[m
[32m+[m[32m        {% endfor %}[m
       </ul>[m
     </div>[m
[31m-  {% endfor %}[m
[31m-  </ul>[m
[31m-  </div>[m
[31m-  <div class="large-4 columns cd-no-padding">[m
[31m-  <div class="cd-spell-sidebar" id="sidebar">[m
[31m-  </div>[m
[31m-  </div>[m
[32m+[m[32m    <div class="large-4 columns cd-no-padding">[m
[32m+[m[32m      <div class="cd-spell-sidebar" id="sidebar"></div>[m
[32m+[m[32m    </div>[m
   </div>[m
   <div class="tabs-panel" id="panel3">[m
[31m-            <ul class="cd-statistics">[m
[31m-            {% for match in character.match_set.all  %}[m
[31m-                <li>[m
[31m-                  <a href="/match/{{ match.id }}/">[m
[31m-                  {{ match.character }} vs {{ match.enemy }}[m
[31m-                  {% if match.enemy_health == 0 %}[m
[31m-                    <span class="success label">Won</span>[m
[31m-                  {% elif match.character_health == 0 %}[m
[31m-                    <span class="alert label">Lost</span>[m
[31m-                  {% else %}[m
[31m-                    <span class="warning label">Unfinished</span>[m
[31m-                  {% endif %}[m
[31m-                  </a>[m
[31m-                </li>[m
[31m-            {% endfor %}[m
[31m-            <!-- <li>{{ level_data.xp_percentage}}% Until Next Level</li> -->[m
[31m-            </ul>[m
[31m-        </div>[m
[31m-            </div> <br>  <br>    <br> [m
[32m+[m[32m    <ul class="cd-statistics">[m
[32m+[m[32m      {% for match in character.match_set.all  %}[m
[32m+[m[32m        <li>[m
[32m+[m[32m          <a href="/match/{{ match.id }}/">[m
[32m+[m[32m            {{ match.character }} vs {{ match.enemy }}[m
[32m+[m[32m            {% if match.enemy_health == 0 %}[m
[32m+[m[32m              <span class="success label">Won</span>[m
[32m+[m[32m            {% elif match.character_health == 0 %}[m
[32m+[m[32m              <span class="alert label">Lost</span>[m
[32m+[m[32m            {% else %}[m
[32m+[m[32m              <span class="warning label">Unfinished</span>[m
[32m+[m[32m            {% endif %}[m
[32m+[m[32m          </a>[m
[32m+[m[32m        </li>[m
[32m+[m[32m      {% endfor %}[m
[32m+[m[32m    </ul>[m
[32m+[m[32m  </div>[m
[32m+[m[32m</div> <br>  <br>    <br>[m[41m [m
 [m
[31m-                <a href="{{ character.get_absolute_url }}/create" class="button">Start Match</a>[m
[32m+[m[32m        <a href="{{ character.get_absolute_url }}/create" class="button">Start Match</a>[m
 [m
[31m-            </div>[m
[31m-        </div>[m
[32m+[m[32m    </div>[m
[32m+[m[32m  </div>[m
 [m
     </div>[m
 {% endwith %}[m
