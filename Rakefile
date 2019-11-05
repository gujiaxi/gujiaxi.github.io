require 'chinese_pinyin'

# usage: rake post['my new post']
desc 'create a new post with "rake post[\'post title\']"'
task :post, [:title] do |t, args|
  if args[:title]
    new_article("_posts", args[:title])
  else
    puts "Please try again. Remember to include the filename."
    exit 1
  end
end

# usage: rake draft['my new draft']
desc 'create a new draft post with "rake draft[\'draft title\']"'
task :draft, [:title] do |t, args|
  if args[:title]
    new_article("_drafts", args[:title])
  else
    puts "Please try again. Remember to include the filename."
    exit 1
  end
end

# usage: rake deploy["option messages"]
desc 'deploy the whole site to the server'
task :deploy, [:msg] do |t, args|
  puts "Deploying site..."
  time = Time.new.strftime("%Y-%m-%d %k:%M:%S")
  if args[:msg]
    msg = args[:msg]
  else
    msg = "Repository deployed by Rakefile at #{time}."
  end
  %x{git add -A && git commit -m "#{msg}" && git push}
  puts "Site deployed: #{msg}"
end

# usage: rake build
task 'build the site'
task :build do
  puts "Building site..."
  %x{jekyll build}
  puts "Site built successfully!"
end

# usage: rake preview
desc 'preview the site with drafts'
task :preview do
  system "jekyll serve --watch --drafts"
end

# usage: rake cleanup
desc 'cleanup jekyll cache'
task :cleanup do
  puts "Cleaning up..."
  %x{jekyll clean}
  puts "Cleanup done!"
end

desc 'list tasks'
task :list do
  puts "Tasks: #{(Rake::Task.tasks - [Rake::Task[:list]]).join(', ')}"
  puts "(type rake -T for more detail)\n\n"
end

# # # # #
# General support functions
# # # # #
def new_article(dir, title)
  _title = title
  title = Pinyin.t(title, splitter: '-').downcase
  filename = "#{dir}/#{Time.now.strftime('%Y-%m-%d')}-#{title}.md"
  puts "Creating new article: #{filename}"
  File.open(filename, "w") do |f|
    f << <<-EOS.gsub(/^    /, '')
    ---
    layout: post
    title: "#{_title}"
    date: #{Time.new.strftime('%Y-%m-%d')}
    ---
    EOS
  end
end
