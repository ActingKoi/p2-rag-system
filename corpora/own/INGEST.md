# Ingest report

Written by `uv run p2 ingest`.
It lists every document in this corpus that ingest added, with what the cleaning pass did and anything that looks wrong.
Running ingest again adds to the table and replaces the "last run" section, and `uv run p2 ingest --report` rewrites it for the documents in docs/ now, after you removed some.

## Summary

- Documents: 410 (the final check needs at least 200)
- Words: 600,434
- Estimated tokens (words times 1.4): 840,607 (`p2 check` warns above 800,000 and fails above 1,000,000)
- Flagged documents: 0

## Documents

| docid | words | characters per page | flags | cleaning |
|---|---:|---:|---|---|
| `anime_.hack_roots` | 2,435 | - | - | - |
| `anime_3_seconds_later_he_turned_into_a_beast` | 285 | - | - | - |
| `anime_absolute_boy` | 805 | - | - | - |
| `anime_afro_samurai` | 2,186 | - | - | - |
| `anime_ah_my_buddha` | 3,357 | - | - | - |
| `anime_aharen-san_is_indecipherable` | 1,361 | - | - | - |
| `anime_air_gear` | 1,246 | - | - | - |
| `anime_air_video_game` | 5,257 | - | - | - |
| `anime_akagi_manga` | 2,397 | - | - | - |
| `anime_akahori_gedou_hour_rabuge` | 368 | - | - | - |
| `anime_akebi_s_sailor_uniform` | 2,019 | - | - | - |
| `anime_akiba_maid_war` | 1,253 | - | - | - |
| `anime_angel_heart_manga` | 1,647 | - | - | - |
| `anime_ani_kuri15` | 541 | - | - | - |
| `anime_animal_yokoch` | 1,815 | - | - | - |
| `anime_aoashi` | 1,890 | - | - | - |
| `anime_aria_manga` | 6,641 | - | - | reference list dropped, 294 characters (heading) |
| `anime_arknights_tv_series` | 1,362 | - | - | - |
| `anime_ascendance_of_a_bookworm` | 1,437 | - | - | - |
| `anime_ayakashi_samurai_horror_tales` | 2,418 | - | - | - |
| `anime_ayakashi_video_game` | 1,181 | - | - | - |
| `anime_baccano` | 4,225 | - | - | - |
| `anime_bak_gyamon` | 298 | - | - | reference list dropped, 486 characters (heading) |
| `anime_bakugan_battle_brawlers` | 3,335 | - | - | - |
| `anime_ballad_of_a_shinigami` | 1,823 | - | - | - |
| `anime_bamboo_blade` | 495 | - | - | - |
| `anime_bang_dream` | 7,227 | - | - | - |
| `anime_bartender_manga` | 1,931 | - | - | - |
| `anime_basilisk_manga` | 828 | - | - | reference list dropped, 382 characters (heading) |
| `anime_battle_b-daman` | 6,430 | - | - | - |
| `anime_beast_tamer` | 1,581 | - | - | - |
| `anime_berserk_the_golden_age_arc` | 2,006 | - | - | - |
| `anime_best_student_council` | 3,531 | - | - | - |
| `anime_bibliophile_princess` | 817 | - | - | - |
| `anime_big_windup` | 3,033 | - | - | - |
| `anime_bikkuriman` | 693 | - | - | - |
| `anime_binb_shimai_monogatari` | 1,075 | - | - | - |
| `anime_binch_-tan_manga` | 1,360 | - | - | - |
| `anime_birdie_wing` | 1,705 | - | - | - |
| `anime_black_blood_brothers` | 3,483 | - | - | reference list dropped, 1,673 characters (heading) |
| `anime_black_cat_manga` | 2,319 | - | - | - |
| `anime_black_jack_manga` | 8,218 | - | - | - |
| `anime_black_rock_shooter` | 1,917 | - | - | - |
| `anime_black_summoner` | 1,455 | - | - | - |
| `anime_bleach_thousand-year_blood_war` | 1,685 | - | - | - |
| `anime_blood` | 2,033 | - | - | - |
| `anime_blue_dragon_tv_series` | 1,569 | - | - | - |
| `anime_blue_drop` | 1,890 | - | - | - |
| `anime_bokurano` | 1,124 | - | - | - |
| `anime_buso_renkin` | 2,034 | - | - | - |
| `anime_buzzer_beater_manga` | 906 | - | - | reference list dropped, 337 characters (heading) |
| `anime_canvas_2_akane-iro_no_palette` | 3,126 | - | - | - |
| `anime_capeta` | 1,882 | - | - | - |
| `anime_chibi_vampire` | 2,170 | - | - | - |
| `anime_chocotto_sister` | 979 | - | - | - |
| `anime_clannad_video_game` | 8,491 | - | - | - |
| `anime_claymore_manga` | 1,619 | - | - | - |
| `anime_cluster_edge` | 317 | - | - | - |
| `anime_code-e` | 1,636 | - | - | - |
| `anime_code_geass` | 5,673 | - | - | - |
| `anime_comic_party` | 3,447 | - | - | - |
| `anime_coyote_ragtime_show` | 2,038 | - | - | - |
| `anime_crash_b-daman` | 2,904 | - | - | - |
| `anime_d.gray-man_tv_series` | 1,769 | - | - | - |
| `anime_d_jin_work` | 1,280 | - | - | - |
| `anime_da_capo_ii` | 3,004 | - | - | reference list dropped, 691 characters (heading) |
| `anime_da_capo_video_game` | 3,022 | - | - | - |
| `anime_damekko_d_butsu` | 804 | - | - | - |
| `anime_dancouga_nova_super_god_beast_armor` | 2,171 | - | - | - |
| `anime_darker_than_black` | 4,222 | - | - | - |
| `anime_death_note_2006_tv_series` | 1,894 | - | - | - |
| `anime_deltora_quest_tv_series` | 3,458 | - | - | - |
| `anime_demonbane` | 2,528 | - | - | - |
| `anime_den-noh_coil` | 4,834 | - | - | - |
| `anime_devil_may_cry_the_animated_series` | 1,397 | - | - | - |
| `anime_di_gi_charat` | 4,253 | - | - | - |
| `anime_doraemon_2005_tv_series` | 2,567 | - | - | - |
| `anime_dragonaut_the_resonance` | 962 | - | - | - |
| `anime_duel_masters` | 4,916 | - | - | - |
| `anime_eagle_talon_tv_series` | 523 | - | - | - |
| `anime_ef_a_fairy_tale_of_the_two` | 4,742 | - | - | - |
| `anime_el_cazador_de_la_bruja` | 1,036 | - | - | - |
| `anime_elemental_gelade` | 3,138 | - | - | - |
| `anime_emma_manga` | 3,036 | - | - | reference list dropped, 318 characters (heading) |
| `anime_engage_planet_kiss_dum` | 532 | - | - | - |
| `anime_ergo_proxy` | 2,761 | - | - | - |
| `anime_eureka_seven` | 3,216 | - | - | - |
| `anime_eyeshield_21` | 3,079 | - | - | - |
| `anime_fantastic_detective_labyrinth` | 1,113 | - | - | - |
| `anime_fate_stay_night` | 5,441 | - | - | reference list dropped, 1,674 characters (heading) |
| `anime_fate_stay_night_2006_tv_series` | 1,166 | - | - | - |
| `anime_fighting_beauty_wulong` | 989 | - | - | - |
| `anime_fist_of_the_blue_sky` | 936 | - | - | - |
| `anime_flag_tv_series` | 416 | - | - | reference list dropped, 1,960 characters (heading) |
| `anime_full_metal_panic` | 3,674 | - | - | - |
| `anime_futakoi_alternative` | 715 | - | - | - |
| `anime_gag_manga_biyori` | 664 | - | - | - |
| `anime_gaiking_legend_of_daiku-maryu` | 684 | - | - | - |
| `anime_gakuen_heaven` | 2,602 | - | - | - |
| `anime_galaxy_angel_ii` | 956 | - | - | - |
| `anime_gallery_fake` | 1,031 | - | - | - |
| `anime_gargoyle_of_yoshinaga_house` | 914 | - | - | - |
| `anime_genesis_of_aquarion` | 1,582 | - | - | - |
| `anime_ghost_hunt_novel_series` | 938 | - | - | - |
| `anime_ghost_slayers_ayashi` | 1,650 | - | - | reference list dropped, 424 characters (heading) |
| `anime_gift_2005_video_game` | 2,790 | - | - | - |
| `anime_gin_iro_no_olynssis` | 408 | - | - | - |
| `anime_ginban_kaleidoscope` | 1,670 | - | - | - |
| `anime_gintama_tv_series` | 2,249 | - | - | - |
| `anime_glass_fleet` | 1,893 | - | - | - |
| `anime_glass_mask` | 2,687 | - | - | reference list dropped, 490 characters (heading) |
| `anime_gun_sword` | 923 | - | - | - |
| `anime_gunparade_march` | 1,053 | - | - | - |
| `anime_guyver_the_bioboosted_armor` | 1,376 | - | - | - |
| `anime_hamtaro` | 536 | - | - | - |
| `anime_hanbun_no_tsuki_ga_noboru_sora` | 1,431 | - | - | - |
| `anime_hanoka` | 272 | - | - | - |
| `anime_happiness_video_game` | 2,323 | - | - | - |
| `anime_happy_seven` | 1,473 | - | - | - |
| `anime_he_is_my_master` | 2,558 | - | - | - |
| `anime_hell_girl` | 1,616 | - | - | - |
| `anime_honey_and_clover` | 1,347 | - | - | reference list dropped, 642 characters (heading) |
| `anime_idaten_jump` | 1,987 | - | - | - |
| `anime_igpx` | 1,707 | - | - | - |
| `anime_izumo_takeki_tsurugi_no_senki` | 325 | - | - | - |
| `anime_jinki_extend` | 2,951 | - | - | reference list dropped, 441 characters (heading) |
| `anime_kaiketsu_zorori` | 820 | - | - | - |
| `anime_kamichu` | 1,304 | - | - | - |
| `anime_la_corda_d_oro` | 850 | - | - | - |
| `anime_le_chevalier_d_eon` | 2,361 | - | - | - |
| `anime_the_familiar_of_zero` | 2,945 | - | - | - |
| `anime_the_galaxy_railways` | 2,799 | - | - | - |
| `anime_the_genie_family` | 1,030 | - | - | - |
| `anime_the_good_witch_of_the_west` | 1,265 | - | - | - |
| `anime_the_king_of_braves_gaogaigar_final` | 1,001 | - | - | - |
| `film_0s_1s` | 264 | - | - | - |
| `film_100_ghost_street_the_return_of_richard_speck` | 519 | - | - | - |
| `film_10_things_i_hate_about_life` | 771 | - | - | - |
| `film_10_years_2011_film` | 920 | - | - | - |
| `film_11-11-11_film` | 1,027 | - | - | - |
| `film_111_first_street_film` | 260 | - | - | - |
| `film_127_hours` | 2,171 | - | - | - |
| `film_13_2010_film` | 1,033 | - | - | - |
| `film_13_the_musical` | 976 | - | - | - |
| `film_16-love` | 925 | - | - | - |
| `film_16_wishes` | 956 | - | - | - |
| `film_17_miracles` | 361 | - | - | reference list dropped, 614 characters (heading) |
| `film_180_2011_american_film` | 839 | - | - | - |
| `film_180_degrees_south_conquerors_of_the_useless` | 899 | - | - | - |
| `film_1946_the_mistranslation_that_shifted_culture` | 639 | - | - | - |
| `film_1_2013_film` | 1,173 | - | - | - |
| `film_1_a_minute` | 340 | - | - | - |
| `film_1_film` | 1,414 | - | - | - |
| `film_2-headed_shark_attack` | 1,189 | - | - | - |
| `film_2000_mules` | 4,241 | - | - | reference list dropped, 173 characters (heading) |
| `film_2001_maniacs_field_of_screams` | 529 | - | - | reference list dropped, 134 characters (heading) |
| `film_200_mph` | 642 | - | - | - |
| `film_2016_obama_s_america` | 1,732 | - | - | reference list dropped, 236 characters (heading) |
| `film_21_jump_street_film` | 2,187 | - | - | - |
| `film_247_f` | 770 | - | - | - |
| `film_25_hill` | 300 | - | - | - |
| `film_28_hotel_rooms` | 630 | - | - | - |
| `film_30_beats` | 585 | - | - | - |
| `film_30_days_of_night_dark_days` | 1,092 | - | - | - |
| `film_30_minutes_or_less` | 1,596 | - | - | - |
| `film_35_and_ticking` | 267 | - | - | - |
| `film_3_2_1._frankie_go_boom` | 280 | - | - | - |
| `film_3_backyards` | 273 | - | - | - |
| `film_3_days_of_normal` | 359 | - | - | - |
| `film_3_minutes` | 312 | - | - | - |
| `film_4_44_last_day_on_earth` | 745 | - | - | - |
| `film_50_50_2011_film` | 1,513 | - | - | - |
| `film_51_film` | 263 | - | - | - |
| `film_5_days_of_war` | 923 | - | - | - |
| `film_5_shells` | 652 | - | - | - |
| `film_6_days_to_air` | 640 | - | - | - |
| `film_6_month_rule` | 806 | - | - | - |
| `film_8213_gacy_house` | 301 | - | - | - |
| `film_8_the_mormon_proposition` | 1,609 | - | - | - |
| `film_96_minutes_2011_film` | 705 | - | - | - |
| `film_9_bullets` | 910 | - | - | - |
| `film_abandoned_2010_film` | 530 | - | - | - |
| `film_abandoned_2022_film` | 780 | - | - | - |
| `film_abandoned_mine` | 288 | - | - | - |
| `film_abby_s_list` | 612 | - | - | - |
| `film_abducted_the_carlina_white_story` | 312 | - | - | - |
| `film_abduction_2011_film` | 1,680 | - | - | - |
| `film_about_cherry` | 370 | - | - | - |
| `film_abraham_lincoln_vampire_hunter` | 1,836 | - | - | - |
| `film_abraham_lincoln_vs._zombies` | 981 | - | - | - |
| `film_absentia_film` | 1,091 | - | - | - |
| `film_accident_man_hitman_s_holiday` | 1,083 | - | - | - |
| `film_across_the_line_the_exodus_of_charlie_wright` | 753 | - | - | - |
| `film_act_of_valor` | 2,035 | - | - | - |
| `film_adventures_of_serial_buddies` | 321 | - | - | - |
| `film_african_cats` | 1,984 | - | - | - |
| `film_after_2012_film` | 2,128 | - | - | - |
| `film_after_ever_happy` | 1,089 | - | - | - |
| `film_after_porn_ends` | 332 | - | - | - |
| `film_after_the_wizard` | 266 | - | - | - |
| `film_aftershock_2012_film` | 895 | - | - | - |
| `film_aftershock_2022_film` | 333 | - | - | - |
| `film_aftersun` | 1,787 | - | - | - |
| `film_age_of_the_dragons` | 694 | - | - | - |
| `film_agent_game` | 449 | - | - | - |
| `film_agents_of_secret_stuff` | 917 | - | - | - |
| `film_ai_weiwei_never_sorry` | 611 | - | - | - |
| `film_air_collision` | 648 | - | - | - |
| `film_airline_disaster` | 655 | - | - | - |
| `film_aisha_2022_film` | 261 | - | - | - |
| `film_akkarakazhchakal_the_movie` | 444 | - | - | - |
| `film_albert_nobbs` | 1,020 | - | - | - |
| `film_alex_cross_film` | 1,198 | - | - | - |
| `film_alice_2022_film` | 537 | - | - | - |
| `film_alice_in_murderland_film` | 293 | - | - | - |
| `film_alice_in_wonderland_2010_film` | 6,259 | - | - | - |
| `film_alien_origin` | 726 | - | - | - |
| `film_aliens_vs._avatars` | 426 | - | - | - |
| `film_all_about_evil` | 1,548 | - | - | - |
| `film_all_god_s_creatures` | 986 | - | - | - |
| `film_all_good_things_film` | 1,458 | - | - | - |
| `film_all_my_friends_are_funeral_singers_film` | 275 | - | - | - |
| `film_all_superheroes_must_die` | 1,198 | - | - | - |
| `film_all_the_light_in_the_sky` | 274 | - | - | - |
| `film_all_things_fall_apart` | 391 | - | - | - |
| `film_allegiance_film` | 572 | - | - | - |
| `film_almost_perfect_film` | 308 | - | - | - |
| `film_alter_egos` | 667 | - | - | - |
| `film_alvin_and_the_chipmunks_chipwrecked` | 1,737 | - | - | - |
| `film_alyce_kills` | 369 | - | - | - |
| `film_amanda_knox_murder_on_trial_in_italy` | 2,119 | - | - | - |
| `film_american_grindhouse` | 292 | - | - | - |
| `film_american_mystic` | 292 | - | - | - |
| `film_american_reunion` | 1,861 | - | - | - |
| `film_american_teacher` | 382 | - | - | - |
| `film_american_warships` | 324 | - | - | - |
| `film_ameriqua` | 2,438 | - | - | - |
| `film_amigo_film` | 788 | - | - | - |
| `film_an_african_election` | 303 | - | - | - |
| `film_an_american_girl_mckenna_shoots_for_the_stars` | 1,385 | - | - | - |
| `film_an_american_mosque` | 493 | - | - | - |
| `film_and_everything_is_going_fine` | 256 | - | - | - |
| `film_and_soon_the_darkness_2010_film` | 599 | - | - | - |
| `film_anderson_s_cross` | 779 | - | - | - |
| `film_anna_may_wong_in_her_own_words` | 773 | - | - | - |
| `film_arcadia_lost` | 349 | - | - | - |
| `film_as_good_as_dead_2010_film` | 407 | - | - | - |
| `film_at_risk_2010_film` | 744 | - | - | - |
| `film_athlete_2010_film` | 300 | - | - | - |
| `film_spy_kids_all_the_time_in_the_world` | 1,873 | - | - | - |
| `film_the_10_commandments_of_chloe` | 1,131 | - | - | - |
| `film_the_12_disasters_of_christmas` | 385 | - | - | - |
| `film_the_19th_wife_film` | 316 | - | - | - |
| `film_the_355` | 2,136 | - | - | - |
| `film_the_41-year-old_virgin_who_knocked_up_sarah_marshall_and_fe` | 752 | - | - | - |
| `film_the_5th_quarter` | 355 | - | - | - |
| `film_the_7_adventures_of_sinbad` | 798 | - | - | - |
| `film_the_a-team_film` | 2,722 | - | - | - |
| `film_the_abcs_of_death` | 643 | - | - | - |
| `film_the_adam_project` | 1,452 | - | - | - |
| `film_the_adjustment_bureau` | 1,769 | - | - | - |
| `film_the_adonis_factor` | 379 | - | - | - |
| `film_the_afflicted_film` | 737 | - | - | - |
| `film_the_agent_2010_film` | 327 | - | - | - |
| `film_the_aggression_scale` | 618 | - | - | - |
| `film_the_amazing_bulk` | 1,592 | - | - | - |
| `film_the_amazing_spider-man_film` | 5,403 | - | - | reference list dropped, 1,780 characters (heading) |
| `film_the_american_2010_film` | 1,577 | - | - | - |
| `film_the_american_scream` | 313 | - | - | - |
| `film_the_amityville_haunting` | 575 | - | - | - |
| `tv_1000_ways_to_die` | 696 | - | - | - |
| `tv_10_items_or_less_tv_series` | 564 | - | - | - |
| `tv_12_corazones` | 671 | - | - | - |
| `tv_1600_pennsylvania_avenue_tv_program` | 633 | - | - | - |
| `tv_1923_tv_series` | 2,293 | - | - | - |
| `tv_19_kids_and_counting` | 3,339 | - | - | - |
| `tv_1_000_places_to_see_before_you_die_tv_series` | 284 | - | - | - |
| `tv_1_vs._100_american_game_show` | 2,268 | - | - | - |
| `tv_1st_look` | 395 | - | - | - |
| `tv_24_7_american_tv_program` | 312 | - | - | - |
| `tv_30_days_tv_series` | 277 | - | - | - |
| `tv_30_rock` | 6,447 | - | - | - |
| `tv_365gay_news` | 305 | - | - | - |
| `tv_3_lbs` | 262 | - | - | - |
| `tv_4real` | 486 | - | - | - |
| `tv_50_cent_the_money_and_the_power` | 347 | - | - | - |
| `tv_61st_street_tv_series` | 651 | - | - | - |
| `tv_8th_ocean` | 287 | - | - | - |
| `tv_90210_tv_series` | 3,521 | - | - | - |
| `tv_acceptable.tv` | 589 | - | - | - |
| `tv_ace_of_cakes` | 707 | - | - | - |
| `tv_acorralada` | 817 | - | - | - |
| `tv_adventure_camp` | 496 | - | - | - |
| `tv_adventure_time` | 9,008 | - | - | - |
| `tv_aew_battle_of_the_belts` | 3,339 | - | - | - |
| `tv_african_american_lives` | 822 | - | - | reference list dropped, 991 characters (heading) |
| `tv_after_words` | 275 | - | - | - |
| `tv_age_of_love_tv_series` | 554 | - | - | - |
| `tv_al_punto` | 899 | - | - | - |
| `tv_alaska_daily` | 611 | - | - | - |
| `tv_alex_wagner_tonight` | 493 | - | - | - |
| `tv_aliens_in_america` | 501 | - | - | - |
| `tv_all_american_homecoming` | 1,314 | - | - | - |
| `tv_all_star_shore` | 2,816 | - | - | - |
| `tv_amarte_as_frijolito` | 1,128 | - | - | - |
| `tv_amazon_music_live` | 593 | - | - | - |
| `tv_america_at_a_crossroads` | 456 | - | - | - |
| `tv_america_s_ballroom_challenge` | 257 | - | - | - |
| `tv_america_s_game_the_super_bowl_champions` | 1,483 | - | - | - |
| `tv_america_s_got_talent` | 8,000 | - | - | - |
| `tv_america_s_got_talent_extreme` | 550 | - | - | - |
| `tv_america_s_heartland` | 436 | - | - | - |
| `tv_america_s_most_smartest_model` | 444 | - | - | - |
| `tv_america_s_newsroom` | 701 | - | - | - |
| `tv_america_s_next_producer` | 518 | - | - | - |
| `tv_america_s_psychic_challenge` | 450 | - | - | - |
| `tv_america_s_test_kitchen_the_next_generation` | 289 | - | - | - |
| `tv_america_the_beautiful_tv_series` | 360 | - | - | - |
| `tv_american_dream_derby` | 292 | - | - | - |
| `tv_american_gangster_tv_series` | 528 | - | - | - |
| `tv_american_gigolo_tv_series` | 655 | - | - | - |
| `tv_american_greed` | 630 | - | - | reference list dropped, 858 characters (heading) |
| `tv_american_heiress` | 487 | - | - | - |
| `tv_american_idol_extra` | 2,281 | - | - | - |
| `tv_american_idol_rewind` | 541 | - | - | - |
| `tv_american_inventor` | 1,067 | - | - | - |
| `tv_american_ninja_challenge` | 841 | - | - | - |
| `tv_amores_de_mercado_2006_tv_series` | 289 | - | - | - |
| `tv_anchorwoman_tv_series` | 341 | - | - | - |
| `tv_andy_barker_p.i` | 928 | - | - | - |
| `tv_anthony_bourdain_no_reservations` | 1,069 | - | - | reference list dropped, 567 characters (heading) |
| `tv_antiques_roadshow_american_tv_program` | 3,638 | - | - | - |
| `tv_are_you_smarter_than_a_5th_grader_american_game_show` | 3,263 | - | - | reference list dropped, 242 characters (heading) |
| `tv_arena_football_league_on_abc` | 376 | - | - | - |
| `tv_arena_football_league_on_espn` | 888 | - | - | - |
| `tv_armed_famous` | 477 | - | - | - |
| `tv_army_wives` | 2,422 | - | - | - |
| `tv_artstar` | 1,333 | - | - | - |
| `tv_as_the_bell_rings_american_tv_series` | 1,018 | - | - | - |
| `tv_astronomy_observations_and_theories` | 646 | - | - | - |
| `tv_attack_of_the_show` | 1,339 | - | - | - |
| `tv_axs_tv_fights` | 931 | - | - | - |
| `tv_b_intune_tv` | 1,903 | - | - | - |
| `tv_back_in_the_day_2006_tv_program` | 281 | - | - | - |
| `tv_back_to_you_tv_series` | 2,162 | - | - | - |
| `tv_bad_girls_club` | 2,682 | - | - | - |
| `tv_bad_girls_road_trip` | 371 | - | - | - |
| `tv_bait_car_tv_series` | 511 | - | - | - |
| `tv_bajo_las_riendas_del_amor` | 359 | - | - | - |
| `tv_barbershop_2005_tv_series` | 693 | - | - | - |
| `tv_battle_of_the_network_reality_stars` | 1,787 | - | - | - |
| `tv_bbc_world_news_america` | 646 | - | - | reference list dropped, 197 characters (heading) |
| `tv_bear_in_the_big_blue_house` | 1,372 | - | - | - |
| `tv_beat_the_blondes` | 397 | - | - | - |
| `tv_beautiful_people_american_tv_series` | 819 | - | - | - |
| `tv_beauty_and_the_geek_american_tv_series` | 940 | - | - | - |
| `tv_being_bobby_brown` | 457 | - | - | - |
| `tv_better_talk_show` | 671 | - | - | - |
| `tv_beyond_the_break` | 359 | - | - | - |
| `tv_big_brother_after_dark` | 977 | - | - | - |
| `tv_big_day` | 305 | - | - | - |
| `tv_big_love` | 6,716 | - | - | - |
| `tv_big_shots_tv_series` | 1,351 | - | - | - |
| `tv_big_spender_tv_series` | 286 | - | - | - |
| `tv_bizarre_foods_with_andrew_zimmern` | 512 | - | - | - |
| `tv_black._white` | 514 | - | - | - |
| `tv_blackbeard_miniseries` | 486 | - | - | - |
| `tv_blade_the_series` | 2,781 | - | - | - |
| `tv_blind_justice_tv_series` | 1,083 | - | - | - |
| `tv_blowin_up` | 528 | - | - | - |
| `tv_bonds_on_bonds` | 330 | - | - | - |
| `tv_bones_tv_series` | 7,029 | - | - | - |
| `tv_boost_mobile_mlg_pro_circuit` | 314 | - | - | - |
| `tv_bozo_gar_and_ray_wgn_tv_classics` | 459 | - | - | - |
| `tv_brat_camp` | 723 | - | - | - |
| `tv_breaking_bonaduce` | 272 | - | - | - |
| `tv_britney_and_kevin_chaotic` | 1,169 | - | - | - |
| `tv_brotherhood_american_tv_series` | 3,133 | - | - | - |
| `tv_brothers_sisters_2006_tv_series` | 2,144 | - | - | - |
| `tv_build_or_bust` | 512 | - | - | - |
| `tv_but_can_they_sing` | 578 | - | - | - |
| `tv_cake_2006_tv_series` | 583 | - | - | - |
| `tv_cash_cab_american_game_show` | 1,961 | - | - | - |
| `tv_cathouse_the_series` | 321 | - | - | reference list dropped, 182 characters (heading) |
| `tv_celebrity_charades` | 538 | - | - | - |
| `tv_dijon_talton` | 547 | - | - | - |
| `tv_donny_deutsch` | 1,031 | - | - | - |
| `tv_el_amor_no_tiene_precio` | 1,082 | - | - | - |
| `tv_la_academia_usa` | 584 | - | - | - |
| `tv_list_of_programs_broadcast_by_tlc` | 337 | - | - | - |
| `tv_out_of_the_wild` | 810 | - | - | - |
| `tv_regular_show` | 3,064 | - | - | - |
| `tv_ruud_kleinpaste` | 280 | - | - | - |
| `tv_spongebob_squarepants` | 8,918 | - | - | reference list dropped, 2,171 characters (heading) |
| `tv_teen_titans_go` | 1,170 | - | - | - |
| `tv_the_5ive` | 280 | - | - | - |
| `tv_the_a-list_2007_tv_series` | 262 | - | - | - |
| `tv_the_academy_american_tv_series` | 543 | - | - | - |
| `tv_the_adam_friedland_show` | 1,322 | - | - | - |
| `tv_the_afterparty_tv_series` | 2,130 | - | - | - |
| `tv_the_amazing_world_of_gumball` | 2,271 | - | - | - |
| `tv_the_apprentice_martha_stewart` | 7,365 | - | - | - |
| `tv_the_bedford_diaries` | 537 | - | - | - |
| `tv_the_big_bang_theory` | 8,400 | - | - | - |
| `tv_the_big_gay_sketch_show` | 1,132 | - | - | - |
| `tv_the_biggest_loser_special_edition` | 685 | - | - | - |
| `tv_the_blitz_tv_program` | 319 | - | - | - |
| `tv_the_book_of_daniel_tv_series` | 720 | - | - | - |
| `tv_the_business_tv_series` | 273 | - | - | - |
| `tv_the_hour_news_hour` | 645 | - | - | - |

## Not added in the last run

Nothing was left out.

## What to check by eye

Ingest cleans text by rules, and rules miss things.
Take five minutes to open the shortest, a middle one and the longest document next to its original and read one page of each.

- Search the documents for `þ`, `¼`, `(cid:` and the replacement character.
  A hit usually means the PDF's font map is wrong, which no tool can repair, so treat it as a defect and leave that document out.
- Look at the end of a few papers.
  Ingest drops a trailing reference list when it finds a References heading or a run of numbered entries.
  A paper whose list has neither can keep it, and then every author and journal name matches queries it should not.
- Open the first lines of a few documents.
  Author lists, copyright pages and tables of contents are not removed automatically, and you may want to cut them.
- Compare one table with the PDF.
  A PDF prints footnote marks as small raised digits, and the converter glues them onto the word or number next to them: `ALUMINUM1` is the heading ALUMINUM with footnote 1, and `11210,000` can be 210,000 with footnote 11.
  Quotes still match the stored text, but a number read from it can be wrong, so check before you trust a figure in a query, a judgment or an answer.
- Fix the `license` column in the manifest for every document, then run `uv run p2 license`.
  It is `unknown` until you do, and `unknown` does not pass.

## If a document is flagged as scanned

A scan is a picture of a page, so there is no text for ingest to read.
This template does not install an OCR tool, because it is large and most students never need it.
If you do need one, the opt-in route is pymupdf4llm with rapidocr, run on its own outside the template's environment:

```
uv run --no-project --with pymupdf4llm --with rapidocr python -c "import pymupdf4llm, sys, pathlib; pathlib.Path(sys.argv[2]).write_text(pymupdf4llm.to_markdown(sys.argv[1], use_ocr=True, force_ocr=True), encoding='utf-8')" scan.pdf scan.md
```

Put the resulting `.md` file in your folder and ingest the folder again.
It costs about 2 seconds a page, and OCR text needs a second look: it misreads ligatures, hyphens and numbers.
pymupdf4llm is AGPL-3.0 software, so use it only as a tool on your own machine, and do not add it to this repo's dependencies or copy its code into the repo.
